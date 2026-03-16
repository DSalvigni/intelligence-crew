# Usa Python leggero
FROM python:3.10-slim

# Imposta la cartella di lavoro nel container
WORKDIR /app

# Installa le dipendenze di sistema necessarie per yfinance e crewai
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installa le librerie Python
RUN pip install --no-cache-dir crewai langchain-ollama yfinance litellm

# Copia il tuo file main.py nella cartella /app del container
COPY main.py .

# Comando per avviare lo script
CMD ["python", "main.py"]