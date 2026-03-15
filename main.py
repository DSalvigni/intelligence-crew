import os
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import tool
import yfinance as yf

# 1. STOP OPENAI PINGS
os.environ["OPENAI_API_KEY"] = "NA"

# 2. DEFINE MICRO MODEL (TinyLlama uses ~800MB RAM)
local_llm = LLM(
    model="ollama/tinyllama",
    base_url="http://127.0.0.1:11434"
)

# 3. TOOL DEFINITION
@tool("stock_price_tool")
def get_stock_data(ticker: str) -> str:
    """Fetch price and 30-day trend for a ticker (e.g., 'AAPL', 'RACE.MI')."""
    try:
        stock = yf.Ticker(ticker.strip().upper())
        hist = stock.history(period="30d")
        if hist.empty: return f"No data for {ticker}"
        price_now = hist['Close'].iloc[-1]
        price_30d = hist['Close'].iloc[0]
        trend = "UP ⬆️" if price_now > price_30d else "DOWN ⬇️"
        return f"{ticker}: {price_now:.2f} ({trend})"
    except Exception as e:
        return f"Error: {str(e)}"

# 4. AGENTS
researcher = Agent(
    role='Financial Researcher',
    goal='Get stock data for NVDA and RACE.MI.',
    backstory='Data expert. You use the stock_price_tool.',
    tools=[get_stock_data],
    llm=local_llm,
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role='Reporting Specialist',
    goal='Create a Markdown table with the data.',
    backstory='Table expert.',
    llm=local_llm,
    verbose=True,
    allow_delegation=False
)

# 5. THE CREW
financial_crew = Crew(
    agents=[researcher, writer],
    tasks=[
        Task(description="Use tool for NVDA and RACE.MI prices.", 
             expected_output="Ticker and price list.", agent=researcher),
        Task(description="Format into a Markdown table.", 
             expected_output="A table.", agent=writer)
    ],
    process=Process.sequential,
    manager_llm=local_llm,
    embedder={
        "provider": "ollama",
        "config": {"model": "tinyllama"}
    }
)

print("\n🚀 [SYSTEM] Starting local analysis with TinyLlama (Micro RAM Mode)...")
print("🚀 [SYSTEM] Using only ~800MB of RAM.\n")

result = financial_crew.kickoff()
print(result)