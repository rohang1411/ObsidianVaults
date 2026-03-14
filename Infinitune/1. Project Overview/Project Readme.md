

**Full Project Title:** InfiniTune: Online Fine Tuning of LLMs using Real Time Data 
**Authors:** Vedant Jhaveri, Rohan Sharma, Nikhil Ravichandran, Akshay Mathur, Erana Wan, Allen Wang 
**Institution:** University of Southern California 

---

## 1. Problem Statement

Current Large Language Models (LLMs) deployed for consumer use are static. They are pre-trained on a fixed dataset and do not learn from new data or user interactions. This is because the computational cost of fully retraining modern, billion-parameter [[4. Transformers Architecture|Transformer]] models is prohibitively high.

As a result, these models rapidly become outdated, or "stale," unable to adapt to evolving real-world events, user preferences, or new information.

## 2. Solution: InfiniTune

InfiniTune is a **production-ready framework for continuous LLM adaptation**. It solves the "model staleness" problem by enabling real-time fine-tuning of an LLM using dynamic data streams.

The 1-minute elevator pitch is:
> "InfiniTune is a system that keeps LLMs up-to-date. It uses [[2. Apache Kafka]] to create a 'conveyor belt' of new data (like live reviews or news). A trainer model continuously learns from this data using an efficient method called [[LoRA]]. It then sends tiny, lightweight updates—also via Kafka—to the live, user-facing LLM, which 'hot-swaps' them without any downtime. This allows the model to learn new information in real-time (e.g., in 60-second intervals)  with minimal computational cost."

## 3. Key Features

* **Real-Time Data Processing:** Ingests and processes dynamic data streams for continuous learning.
* **Efficient Fine-Tuning:** Employs [[4. QLoRA]]  and [[3. LoRA (Low-Rank Adaptation)|LoRA]]  to fine-tune models, reducing trainable parameters by 1000x compared to full fine-tuning  and preserving 91.05% of base model parameters.
* **Low-Latency Updates:** Features hot-swappable LoRA adapters, allowing the live inference server to update its knowledge with a latency as low as 60 seconds.
* **Decoupled Architecture:** The system is broken into three distinct modules: a data producer, a trainer, and an inference server, which communicate via Kafka.
* **Synchronized & Distributed:** Uses a novel Kafka-based weight update protocol to synchronize model updates across distributed inference endpoints.
* **User Interface:** Includes a front-end UI  and a [[1. Flask]] API  for easy querying and interaction with the updated model.

## 4. Tech Stack

* **Core Language:** Python
* **Data Streaming:** [[2. Apache Kafka]] 
* **ML Framework:** [[3. PyTorch]]
* **LLM Library:** [[2. Hugging Face Transformers]] 
* **PEFT Library:** Hugging Face `peft`
* **Fine-Tuning Technique:** [[3. LoRA (Low-Rank Adaptation)|LoRA]] , [[4. QLoRA]] 
* **Base Model:** Qwen2.5-1.5B-Instruct 
* **API / Serving:** [[1. Flask]] 
* **Configuration:** YAML (unified configuration system) 
* **Evaluation Metric:** [[1. Perplexity (Metric)]] 
* **Planned Deployment:** [[1. Docker]] & [[2. Kubernetes]] 

## 5. Project Structure Map

(Based on files referenced in the report and presentation )

```
Infinitune-Realtime-LLM-Fine-Tuning-Framework/
├── requirements.txt        # Project dependencies
├── config.yaml             # Unified configuration for model, Kafka, LoRA 
├── producer.py             # Data Generator: reads data and streams to Kafka 
├── dataset.py              # Helper for loading and processing datasets 
├── finetune.py             # Core fine-tuning logic 
├── trainer.py              # Consumes from Kafka, runs training loop, produces weights 
├── inference.py            # Core logic for model inference 
├── inference_api.py        # Flask API endpoint to serve prompts and hot-swap weights 
└── ... (other project files)
```