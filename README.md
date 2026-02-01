# 🧠 AI Research Intelligence Agent

> **From Chaos to Clarity: An End-to-End Autonomous Market Research Analyst**

## 📖 Overview

This project is not just a chatbot; it is a **Research-First Decision Support System**. It automates the messy, fragmented workflow of market research by unifying qualitative data (transcripts, feedback) and quantitative data (CSVs, metrics) into a single intelligent engine.

Unlike standard LLMs that hallucinate or provide surface-level summaries, this agent uses a **Bicameral Architecture**—separating the *"Reasoning Brain"* (Logic) from the *"Data Engine"* (Math)—to ensure every insight is traceable, fact-checked, and statistically grounded.

---

## 🛑 The Problem

Market research today is broken and labor-intensive:

* **Fragmented Workflows:** Analysts juggle audio transcripts in one tool and Excel spreadsheets in another, manually stitching together the "What" (Data) and the "Why" (Sentiment).
* **The "Black Box" Issue:** Generative AI is often untrustworthy for business because it invents facts.
* **Analysis Paralysis:** Stakeholders are overwhelmed by data dumps instead of receiving actionable, prioritized insights.

---

## 🏗️ Our Solution: The "Agent Controller" Architecture

We solved this by building a modular system with three distinct roles:

### 1. 🧠 The Brain (Person 1: Agent Reasoning)
* **Role:** The Project Manager & Quality Controller.
* **Function:** It does not do the math. Instead, it orchestrates the conversation, detects user intent (e.g., "Launch" vs. "Retention"), and selects the right tools.
* **Innovation:** Uses a **"4-Signal Clarity Check"** (Coverage, Risk, Structure, Value). It will refuse to output an answer if it doesn't meet strict clarity standards, escalating to prioritization or summary modes instead.

### 2. ⚙️ The Engine (Person 2: Data Intelligence)
* **Role:** The Calculator & Vault.
* **Function:** A deterministic engine that ingests raw files (CSV/Text), normalizes them via a Canonical Data System, and stores them in a Vector Database (ChromaDB) and Structured Store (Pandas).
* **Innovation:** Executes rigorous statistical analysis (churn calculation, market sizing) without LLM variance.

### 3. 💻 The Interface (Person 3: Frontend UI)
* **Role:** The Presenter.
* **Function:** A Streamlit-based UI that handles file ingestion and state management.
* **Innovation:** Features a **"Handover Mechanism"**—when a file is uploaded, the agent pauses to confirm understanding before rushing to analysis, mimicking a human analyst's workflow.

---

## ⚡ Key Features

* **🎯 Goal-Anchored Research:** The agent never chatters aimlessly. Every interaction maps to one of 7 predefined goals (e.g., Launch, Performance, UX).
* **🔄 Sequential Goal Queueing:** Handles complex multi-part questions by queueing them (e.g., "I'll analyze Pricing first, then move to Competitors").
* **🔍 Traceability:** Every insight cites its source. _"Churn is up 15%"_ is accompanied by _"Calculated via scan_kpi_health tool on hairfall.csv."_
* **📉 Progressive Disclosure:** The UI adapts depth—offering "Summaries" for executives and "Deep Evidence" for analysts.

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Core Logic** | Python 3.10+ |
| **Orchestration** | LangChain |
| **LLM** | OpenAI GPT-4 Turbo |
| **Data Processing** | Pandas, NumPy |
| **Vector Database** | ChromaDB (Semantic Search) |
| **Frontend** | Streamlit |
| **Validation** | Pydantic |

---

## 📂 File Structure

```text
ai-research-intelligence/
├── agent_reasoning/       # Person 1: Logic, Prompts, & Orchestration
│   ├── brain.py           # Main reasoning loop
│   └── tools.py           # Clarity checks & tool selection
├── data_intelligence/     # Person 2: Math Engines & Vector Store
│   ├── quant_engine.py    # Pandas/NumPy analysis
│   └── vector_store.py    # ChromaDB management
├── frontend_ui/           # Person 3: Streamlit Interface
│   ├── app.py             # Main UI entry point
│   └── components/        # UI widgets
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation

## 👥 Team Members

* **Suchet Goel**
* **Rohit Kumar Jha**
* **Vaishnavi Shinde**