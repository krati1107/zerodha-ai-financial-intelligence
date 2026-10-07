from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from pathlib import Path
import os
from services.llm_service import generate_portfolio_insight

app = FastAPI(title="Zerodha AI Financial Intelligence Platform")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok", "service": "zerodha-ai-backend"}

@app.post("/api/portfolio-analysis")
def portfolio_analysis():
    data_path = Path(__file__).resolve().parents[1] / "data" / "sample_portfolios.csv"
    df = pd.read_csv(data_path)

    df["value"] = df["quantity"] * df["current_price"]
    df["pnl"] = (df["current_price"] - df["avg_price"]) * df["quantity"]
    total_value = df["value"].sum()
    df["allocation"] = df["value"] / total_value * 100

    sector = df.groupby("sector")["value"].sum().reset_index()
    sector["allocation"] = sector["value"] / total_value * 100

    return {
        "total_value": total_value,
        "holdings": df.to_dict(orient="records"),
        "sector_allocation": sector.to_dict(orient="records"),
        "top_movers": df.sort_values("pnl", ascending=False).head(3).to_dict(orient="records")
    }

@app.post("/api/insights/generate")
def generate_insight(metrics: dict):
    insight = generate_portfolio_insight(metrics)
    return {"insight": insight}
