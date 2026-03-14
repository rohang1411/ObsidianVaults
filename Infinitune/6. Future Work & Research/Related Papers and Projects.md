

This document provides a list of cutting-edge research and open-source projects that are conceptually related to InfiniTune's goal of real-time or continuous model adaptation.

## 1. Related Research Papers

### 📄 Online Training of Large Language Models: Learn while Chatting
* **Link:** 

```embed
title: "Online Training of Large Language Models: Learn while Chatting"
image: "https://imgs.search.brave.com/_IoA22pp30g3Ho2Vfc_qa95Q-c0Ngd461BEoLBrL3iA/rs:fit:200:200:1:0/g:ce/aHR0cHM6Ly9wYXBl/ci1hc3NldHMuYWxw/aGF4aXYub3JnL2lt/YWdlLzI0MDMuMDQ3/OTB2MS5wbmc"
description: ""
url: "https://arxiv.org/pdf/2403.04790v1"
favicon: ""
```



* **Relevance to InfiniTune:** This paper directly addresses the same core problem. It proposes a new paradigm called "Online Training using External Interactions" which, like InfiniTune, aims to create a model that can learn and evolve in real-time in response to human input and external data. It formally classifies the different methods of incremental learning (offline vs. online) and argues for a user-friendly, persistent learning methodology, which is exactly what InfiniTune aims to build.

### 📄 Fine-Tuning Methods for LLMs in Clinical Medicine (SFT vs. DPO)
* **Link:** 
* 
```embed
title: "             Fine-Tuning Methods for Large Language Models in Clinical Medicine by Supervised Fine-Tuning and Direct Preference Optimization: Comparative Evaluation - PMC         "
image: "https://cdn.ncbi.nlm.nih.gov/pmc/banners/logo-jmir.png"
description: "Large language model (LLM) fine-tuning is the process of adjusting out-of-the-box model weights using a dataset of interest. Fine-tuning can be a powerful technique to improve model performance in fields like medicine, where LLMs may have poor ..."
url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC12457693/"
favicon: ""
aspectRatio: "15"
```

* **Relevance to InfiniTune:** While InfiniTune focuses on *how* to deliver the updates (the streaming architecture), this paper provides a deep dive into *what* is being delivered. InfiniTune uses Supervised Fine-Tuning (SFT) on the IMDB data. This paper compares SFT with a more advanced method called Direct Preference Optimization (DPO). This represents a clear "next step" for the `QLORA Trainer` module—it could be upgraded from simple SFT to DPO to achieve even better performance from the real-time data.

## 2. Related Open-Source Projects

### 🚀 LLaMA-Factory
* **Link:** 

```embed
title: "GitHub - hiyouga/LLaMA-Factory: Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024)"
image: "https://repository-images.githubusercontent.com/646410686/ccb14d87-7454-4e82-a85c-f1f63a3c1ccb"
description: "Unified Efficient Fine-Tuning of 100+ LLMs & VLMs (ACL 2024) - hiyouga/LLaMA-Factory"
url: "https://github.com/hiyouga/LLaMA-Factory"
favicon: ""
aspectRatio: "50"
```



* **Relevance to InfiniTune:** This is a comprehensive, "one-stop" toolkit for fine-tuning 100+ different LLMs. It is highly relevant to the `QLORA Trainer` component. It provides a robust, pre-built, and highly optimized library for performing many types of PEFT, including [[4. QLoRA]], as well as advanced algorithms like DPO. The InfiniTune `trainer.py` script could potentially be simplified and made more powerful by integrating LLaMA-Factory as its training backend instead of a custom [[3. PyTorch]] loop.

### 🚀 LangChain / LlamaIndex

* **Link (LangChain):**

```embed
title: "GitHub - langchain-ai/langchain: 🦜🔗 The platform for reliable agents."
image: "https://repository-images.githubusercontent.com/552661142/7ce81c9c-d475-4425-8fa6-ec21021a6b1a"
description: "🦜🔗 The platform for reliable agents. Contribute to langchain-ai/langchain development by creating an account on GitHub."
url: "https://github.com/langchain-ai/langchain"
favicon: ""
aspectRatio: "50"
```


* **Link (Llama Index):** 

```embed
title: "GitHub - run-llama/llama_index: LlamaIndex is the leading framework for building LLM-powered agents over your data."
image: "https://opengraph.githubassets.com/7e87a2e7a853457f527215c68d80dbaccb7ae65b77a31038e23f871ce513be2e/run-llama/llama_index"
description: "LlamaIndex is the leading framework for building LLM-powered agents over your data. - run-llama/llama_index"
url: "https://github.com/run-llama/llama_index"
favicon: ""
aspectRatio: "50"
```


* **Relevance to InfiniTune:** These projects tackle the "model staleness" problem from a *different angle*, known as **Retrieval-Augmented Generation (RAG)**.
    * **InfiniTune's method (Fine-Tuning):** "Let's *teach* the model the new information by updating its weights."
    * **RAG's method (In-Context Learning):** "Let's *show* the model the new information." When a user asks a question, the RAG system first searches a vector database for relevant *new* documents, and then "stuffs" those documents into the prompt as context for the LLM.
    * **Why it's related:** RAG is the primary *alternative* to InfiniTune's approach. A powerful future research direction would be to *combine* them: using InfiniTune to continuously fine-tune a model on the *patterns* of the data stream, while using RAG to provide specific, up-to-the-second *facts*.