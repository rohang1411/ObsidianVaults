

This document outlines the planned future work for the InfiniTune project, as specified in the "Future Progress" and "Future Work" sections of the project report and presentation.

## 1. Immediate Next Steps

* **User Interface:** Develop a frontend UI for interacting with the fine-tuned model via the [[1. Flask]] inference service.

## 2. Post-Semester / Long-Term Goals

### 🧠 Intelligent Weight Updates
* **Idea:** Design a selective algorithm to push *only* the most relevant or significant weight changes, rather than the entire [[3. LoRA (Low-Rank Adaptation)|LoRA]] adapter every time.
* **Reason:** This would optimize bandwidth and further reduce latency.
* **Implementation:** This would be supplemented by periodic full-model syncs to ensure no drift over time.

### ⚡ Performance Optimization
* **Idea:** Rewrite the core training and inference components in a lower-level language like C++.
* **Reason:** To achieve production-level speed and memory efficiency beyond what Python can offer.

### 📈 Model Scalability
* **Idea:** Implement a [[3. Parameter Server]] architecture.
* **Reason:** To overcome the message size limitations of [[2. Apache Kafka]]. This is the main bottleneck preventing the framework from scaling to larger models (e.g., 70B+), as their [[3. LoRA (Low-Rank Adaptation)|LoRA]] adapters would be too large for a standard Kafka message.

### 🚢 Production Readiness (Deployment)
* **Idea:** Containerize the entire pipeline using [[1. Docker]].
* **Reason:** To ensure robust, portable, and reproducible deployment.
* **Implementation:** Use [[2. Kubernetes]] for orchestration, which would automatically manage scheduling, auto-scaling (e.g., of the inference server), and fault tolerance (e.g., automatically restarting a failed component).