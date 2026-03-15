import os
from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama # Più robusto per test rapidi
from crewai.tools import tool
import yfinance as yf

# Forza il bypass di OpenAI
os.environ["OPENAI_API_KEY"] = "NA"

# CONFIGURAZIONE LLM - Puntiamo dritti all'IP locale
local_llm = Ollama(model="llama3", base_url="http://127.0.0.1:11434")

@tool("stock_price_tool")
def get_stock_data(ticker: str) -> str:
    """Gets stock price and trend."""
    try:
        stock = yf.Ticker(ticker.strip().upper())
        hist = stock.history(period="30d")
        if hist.empty: return f"No data for {ticker}"
        price = hist['Close'].iloc[-1]
        trend = "UP" if price > hist['Close'].iloc[0] else "DOWN"
        return f"{ticker}: {price:.2f} ({trend})"
    except:
        return f"Error on {ticker}"

researcher = Agent(
    role='Researcher',
    goal='Get stock data for AAPL and RACE.MI',
    backstory='Data collector.',
    tools=[get_stock_data],
    llm=local_llm,
    verbose=True
)

task = Task(description="Get price for AAPL and RACE.MI", expected_output="Prices", agent=researcher)

crew = Crew(agents=[researcher], tasks=[task], process=Process.sequential)

print("\n🚀 Ora Ollama è attivo. Lancio l'agente...\n")
print(crew.kickoff())