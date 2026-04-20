# 🛒 E-Commerce FAQ Bot using Agentic AI

## 📌 Overview

This project is an intelligent **E-commerce FAQ Assistant** built using an Agentic AI architecture.
It answers customer queries related to shipping, returns, refunds, and policies using a **Retrieval-Augmented Generation (RAG)** approach.

The system uses **LangGraph** for orchestration, **ChromaDB** for document retrieval, and **Groq LLM API** for generating responses.

---

## 🎯 Features

* ✅ Accurate answers from knowledge base
* ✅ Multi-turn conversation memory (thread_id)
* ✅ Intelligent routing (retrieve / tool / skip)
* ✅ Tool support (date/time queries)
* ✅ Self-evaluation (faithfulness scoring)
* ✅ No hallucination design
* ✅ CLI + Streamlit UI

---

## 🏗️ Project Structure

```
ecommerce_faq_bot/
│
├── .env
├── data/
│   ├── documents.py
│   └── embeddings.py
│
├── ecommerce_assistant/
│   ├── state.py
│   ├── nodes.py
│   ├── tools.py
│   ├── graph.py
│   └── llm.py
│
├── tests/
│   └── test_agent.py
│
├── agent.py
├── capstone_streamlit.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* LangGraph
* ChromaDB
* Groq API (LLM)
* Sentence Transformers
* Streamlit

---

## 🔐 Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd ecommerce_faq_bot
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file in root:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Running the Project

### 🔹 CLI Mode

```
python agent.py
```

### 🔹 Streamlit UI

```
streamlit run capstone_streamlit.py
```

---

## 🧠 How It Works

Flow:

```
User → Memory → Router → (Retrieve / Tool / Skip)
     → Answer → Eval → Save → END
```

### Components:

* **Memory Node** → Stores conversation
* **Router Node** → Decides action
* **Retrieval Node** → Fetches context
* **Tool Node** → Handles dynamic queries
* **Answer Node** → Generates response
* **Eval Node** → Checks faithfulness
* **Save Node** → Updates state

---

## 📚 Knowledge Base

* 10 domain-specific documents
* Covers:

  * Shipping policy
  * Return policy
  * Refund process
  * Payment methods
  * Order tracking
  * Cancellation rules

---

## 🧪 Testing

* ✔ Normal queries
* ✔ Memory recall
* ✔ Tool usage
* ✔ Out-of-scope handling
* ✔ Prompt injection resistance

---

## 📊 Results

* ✔ Accurate responses from KB
* ✔ Faithfulness score ~0.8
* ✔ Correct routing decisions
* ✔ Memory retention across turns

---

## 🚀 Future Improvements

* Multilingual support
* Real API integration (order tracking)
* UI improvements
* Better retrieval precision
* Cloud deployment

---

## 📌 Conclusion

This project demonstrates how Agentic AI can automate customer support efficiently using structured knowledge, memory, and intelligent decision-making.

---
