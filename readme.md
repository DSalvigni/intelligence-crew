


Ecco il tuo contenuto formattato come un file README.md pulito e professionale:
markdown
Copy

# 📈 AI Stock Intelligence Crew

**Autonomous market analysis system** using **CrewAI** and **Ollama**.
Monitors global stocks with **zero API costs** by running everything on your local hardware.

---

## 🎯 Project Objective

Automate performance research for the **top 10 companies** across:
- USA (NYSE)
- Japan (TSE)
- Italy (Borsa Italiana)

The system calculates **30-day trends** and uses a local AI agent to generate a **professional financial report**.

---

## 🛠️ Tech Stack
   Component      | Technology                                                                 |
 |----------------|----------------------------------------------------------------------------|
 | Orchestrator   | [CrewAI](https://www.crewai.com/)                                         |
 | Local LLM       | [Ollama](https://ollama.com/) (Phi-3 Mini)                                |
 | Data Engine     | `yfinance` (scrapes Yahoo Finance directly)                               |
 | Environment    | Docker (Linux optimized)                                                   |

---

## 🚀 Setup & Execution (Linux)

### 1. Prepare the Local LLM (Ollama)

Install Ollama and pull the lightweight Phi-3 model:
```bash
ollama pull phi3
```

### 2. Allow Docker to communicate with Ollama, expose the service:
bash
Copy
```bash
sudo systemctl edit ollama.service
```

Add the following lines:
```bash
[Service]
Environment="OLLAMA_HOST=0.0.0.0"
```

Restart the service:
```bash
sudo systemctl daemon-reload && sudo systemctl restart ollama
```

### 3. Build the Container
```bash
docker build -t stock-intelligence-crew .
```

### 4. Launch the Agents
```bash
docker run --network="host" stock-intelligence-crew
```

### Miscellaneus
⚙️ Performance & Privacy

RAM Optimization: Uses Phi-3 Mini (2.2GB), runs within 2.5GB-3GB RAM constraints.
Host Networking: Uses --network="host" to bypass Docker bridge latency and DNS issues on Linux.
Privacy: 100% local. No financial data or prompts are sent to external cloud providers.

📊 Report Legend  
      Indicator
      Meaning    
      ⬆️ UP / ⬇️ DOWN
      Price trend over the last 30 trading days
    
      🟢 BULLISH
      Growth momentum > 1.5%. Positive outlook
    
      🔴 BEARISH
      Negative momentum < -1.5%. Caution advised
    
      🟡 STABLE
      Sideways movement within +/- 1.5% range
    



⚠️ Troubleshooting

->    Connection Refused
      Ensure Ollama is listening on 0.0.0.0: ss -tulpn | grep 11434
    
->    Model Not Found
      Verify model with ollama list
    
->    Out of Memory
      Close heavy applications (e.g. Chrome) before running the agents
    

⚠️ Disclaimer
This project is for educational purposes only by @DSalvigni





