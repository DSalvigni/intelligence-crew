import os
import yfinance as yf
from crewai import Agent, Task, Crew, LLM

os.environ["OPENAI_API_KEY"] = "NA"

# CONFIGURAZIONE LLM - Usiamo Phi-3 (che hai già!)
local_llm = LLM(
    model="ollama/phi3:latest", 
    base_url="http://127.0.0.1:11434", # Se usi --network="host"
    temperature=0.1
)

def get_market_data():
    tickers = ["AAPL", "NVDA", "TSLA", "MSFT", "AMZN", "RACE.MI", "ISP.MI", "ENI.MI", "7203.T", "9984.T"]
    results = []
    print("⏳ Estrazione dati reali...")
    for t in tickers:
        try:
            stock = yf.Ticker(t)
            h = stock.history(period="35d")
            if len(h) < 30: continue
            p_now = h['Close'].iloc[-1]
            p_old = h['Close'].iloc[-30]
            diff = ((p_now - p_old) / p_old) * 100
            trend = "UP ⬆️" if diff > 0 else "DOWN ⬇️"
            forecast = "BULLISH 🟢" if diff > 1.5 else "BEARISH 🔴" if diff < -1.5 else "STABLE 🟡"
            results.append(f"| {t} | {p_now:.2f} | {trend} ({diff:.1f}%) | {forecast} |")
        except: continue
    return "\n".join(results)

table_rows = get_market_data()

reporter = Agent(
    role='Financial Reporter',
    goal='Format the stock data into a clean Markdown table.',
    backstory='You are an expert in financial formatting.',
    llm=local_llm,
    verbose=True
)

task = Task(
    description=f"Create a Markdown table with these rows:\n{table_rows}\nHeaders: | Ticker | Price | Trend (30d) | Forecast |",
    expected_output="A clean markdown table.",
    agent=reporter
)

crew = Crew(agents=[reporter], tasks=[task])
print(crew.kickoff())