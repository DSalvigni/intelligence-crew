# 📈 AI Stock Intelligence Crew

An autonomous AI agent system designed to monitor global stock markets (**USA, Japan, Italy**) without any external API costs. This project leverages **CrewAI** for orchestration and **Ollama** for running Large Language Models (LLMs) locally.

---

## 🎯 Project Objective
The goal is to automate the performance research of the top 10 companies by market capitalization across three major markets. The system calculates the 30-day price trend and generates a comparative table with visual indicators (⬆️/⬇️).

## 🛠️ Tech Stack & Definitions
* **Orchestrator (CrewAI):** An open-source framework for orchestrating role-playing autonomous AI agents.
* **Local LLM (Ollama):** A tool that allows you to run open-source models (like Llama 3 or Mistral) locally on your machine, ensuring privacy and zero costs.
* **Data Source (yfinance):** A Python library that scrapes data from Yahoo Finance, bypassing the need for expensive financial API keys.

---

## ⚙️ Installation & Setup

### 1. Install Local LLM
Download and install Ollama from [ollama.com](https://ollama.com). Once installed, download the model by running this command in your terminal:
```bash
ollama run llama3