"""
Portfolio Analysis API
Handles portfolio data ingestion and analytics computation.
"""
from fastapi import APIRouter, HTTPException
from pathlib import Path
import pandas as pd

router = APIRouter(prefix="/api/portfolio", tags=["Portfolio"])


@router.post("/analysis")
def portfolio_analysis(portfolio_id: str = "default"):
    """
    Computes portfolio metrics: total value, P&L, allocation, sector split.
    """
    try:
        data_path = Path(__file__).resolve().parents[2] / "data" / "sample_portfolios.csv"
        df = pd.read_csv(data_path)

        df["value"] = df["quantity"] * df["current_price"]
        df["pnl"] = (df["current_price"] - df["avg_price"]) * df["quantity"]
        total_value = df["value"].sum()
        df["allocation"] = df["value"] / total_value * 100

        sector = df.groupby("sector")["value"].sum().reset_index()
        sector["allocation"] = sector["value"] / total_value * 100

        return {
            "status": "success",
            "portfolio_id": portfolio_id,
            "total_value": float(total_value),
            "holdings": df.to_dict(orient="records"),
            "sector_allocation": sector.to_dict(orient="records"),
            "top_movers": df.sort_values("pnl", ascending=False).head(3).to_dict(orient="records"),
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Portfolio data file not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
