
This guide provides potential interview questions and strong, structured answers based *specifically* on the InfiniTune project.

## 1. Behavioral Questions

### "Tell me about a major challenge you faced in this project."
* **Answer:** "A major challenge was ensuring the real-time 'hot-swap' of the model weights on the inference server worked without any downtime or request failures. The inference server is a live [[1. Flask]] API serving user prompts, and in the background, a separate thread is consuming from a [[2. Apache Kafka|Kafka]] topic waiting for new [[3. LoRA (Low-Rank Adaptation)|LoRA]] weights."
* **Challenge:** "The challenge was one of concurrency: how do you safely modify the model's weights (a critical resource) while the *main thread* is actively using that same model to make predictions?"
* **Solution:** "We solved this by implementing a thread-safe mechanism. The background consumer thread loads the new weights into a temporary variable, and then, using a thread lock, it can update the model's state dictionary in one atomic operation. This ensures the main API thread never tries to access the model *during* an update, preventing corrupted predictions and ensuring uninterrupted service."

### "Tell me about a key architectural decision you made."
* **Answer:** "A key decision was to use [[2. Apache Kafka]] for *two* distinct purposes, not just one. It wasn't just a data ingestion pipeline; we also used it as a **model weight propagation protocol**."
* **Alternatives:** "We could have had the inference server periodically poll a file storage (like S3) or a database for new weights. Or the trainer could have made a direct API call to the inference server."
* **Reasoning:** "Using Kafka as a [[1. Pub-Sub Model (Publish-Subscribe Model)|pub-sub]] queue for weights was far more scalable and decoupled. It allows for a 'fan-out' architecture: our one `QLORA Trainer` can publish a weight update to the `lora_weights` topic, and 100 distributed `Inference Server` replicas could *all* consume that update simultaneously and independently. This is much more resilient and performant than a direct API call and allowed us to achieve synchronized model evolution across all endpoints."

## 2. Technical Questions

### "Why did you choose [[4. QLoRA]] instead of full fine-tuning?"
* **Answer:** "It came down to feasibility. Our goal was *online* fine-tuning in near real-time, on the order of 60-second intervals.
* **Full Fine-Tuning:** "Fully fine-tuning all 1.5 billion parameters of the Qwen2.5 model would be computationally impossible in that time frame. It would require massive GPU resources and would be far too slow."
* **QLoRA:** "[[4. QLoRA]] was the solution for two reasons:
    1.  **Parameter-Efficiency:** It reduced the number of trainable parameters by 1000x, so we were only training a tiny set of adapter weights.
    2.  **Memory-Efficiency:** The 'Q' (quantization) was critical. It allowed us to run the entire training process on a single 12GB RTX 4080 laptop GPU by quantizing the massive base model to 4-bits. Without [[4. QLoRA]], this project would not have been possible on our available hardware."

### "Walk me through the data flow for a single training update."
* **Answer:** "Certainly. It's a two-stage flow:
    1.  **Data Ingestion:** First, the `Data Generator` (`producer.py`) reads a sample from the IMDB dataset and publishes it as a message to the `training_data` Kafka topic. The `QLORA Trainer` (`trainer.py`) is subscribed to this topic, consumes the message, adds it to a mini-batch, and performs a training step to update its local LoRA adapter.
    2.  **Weight Propagation:** After 60 seconds, the `QLORA Trainer` *switches roles*. It packages its newly trained LoRA adapter weights and publishes them as a new message to the *second* Kafka topic, `lora_weights`.
    3.  **Hot-Swap:** Finally, the `Inference Server` (`inference_api.py`), which is subscribed to the `lora_weights` topic, consumes this new weight message and immediately loads it into the live model in memory, completing the update."

## 3. Design Questions

### "How would you scale this project to handle larger models, as you mentioned in your 'Future Work'?"
* **Answer:** "Our report identifies two main bottlenecks for scaling: Kafka's message size and training speed.
    1.  **Scaling Weight Updates:** "Right now, we're sending the *entire* LoRA adapter file over Kafka. For a 70B model, this file could be too large for a message. Our proposed solution is to implement a [[3. Parameter Server]] architecture. The trainer would 'push' weight updates to this central server, and all inference nodes would 'pull' the latest parameters. This is a much more robust pattern for distributing large model parameters than Kafka."
    2.  **Scaling Training/Inference:** "To improve speed, our report suggests rewriting the core training and inference components in C++. For deployment, we'd containerize all three services using [[1. Docker]] and manage them with [[2. Kubernetes]]. This would allow us to automatically scale the `Inference Server` horizontally to handle user load and to intelligently 'schedule' the expensive `QLORA Trainer` container onto dedicated GPU nodes."