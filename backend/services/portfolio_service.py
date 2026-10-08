"""
Portfolio Service
Business logic for portfolio calculations.
"""
import pandas as pd


def calculate_portfolio_metrics(df: pd.DataFrame) -> dict:
    """Computes all portfolio metrics from holdings dataframe."""
    df = df.copy()
    df["value"] = df["quantity"] * df["current_price"]
    df["pnl"] = (df["current_price"] - df["avg_price"]) * df["quantity"]
    total = df["value"].sum()

    df["allocation"] = df["value"] / total * 100

    weights = df["allocation"] / 100
    hhi = float((weights ** 2).sum())

    sector = df.groupby("sector")["value"].sum().reset_index()
    sector["allocation"] = sector["value"] / total * 100
    sector_list = sector.sort_values("allocation", ascending=False).to_dict("records")

    top3 = float(df.nlargest(3, "allocation")["allocation"].sum())

    return {
        "total_value": float(total),
        "pnl": float(df["pnl"].sum()),
        "holdings": df.to_dict("records"),
        "sector_allocation": sector_list,
        "hhi": hhi,
        "top3_concentration": top3,
    }
