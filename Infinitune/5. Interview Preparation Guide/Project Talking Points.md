# For Resumes or Cover Letters

Here are bulleted "brag points" that can be adapted for a resume, cover letter, or elevator pitch.

### High-Impact Points
* Engineered **InfiniTune**, a production-ready, real-time [[1. Fine-Tuning]] framework for [[1. Large Language Models (LLMs)]] to combat model staleness.
* Designed a novel, [[2. Apache Kafka|Kafka-based]] weight update protocol to propagate [[3. LoRA (Low-Rank Adaptation)|LoRA]] adapters to distributed inference servers with **~60-second update latency**.
* Achieved an **8.13% reduction in model perplexity** (from 24.10 to 22.14) by continuously fine-tuning a 1.5B parameter LLM on a live data stream.

### Technical & Architectural Points
* Architected a decoupled, three-component system (Producer, Trainer, Server) using a [[1. Pub-Sub Model (Publish-Subscribe Model)|pub-sub]] model to ensure modularity and scalability.
* Implemented a [[4. QLoRA]] training pipeline to efficiently fine-tune a 1.5B parameter LLM on a **single 12GB consumer GPU** by leveraging 4-bit quantization.
* Developed a multi-threaded [[1. Flask]] API server capable of "hot-swapping" model weights in real-time with zero downtime, ensuring uninterrupted inference.
* Utilized a unified YAML-based configuration system to manage all parameters for [[2. Apache Kafka]], [[3. LoRA (Low-Rank Adaptation)|LoRA]], and model selection, enabling flexible deployment.
* Quantitatively validated model adaptation, proving the system's effectiveness through perplexity tracking, and qualitatively demonstrated it by correcting factual hallucinations in the base model.