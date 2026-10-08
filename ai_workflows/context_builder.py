"""
Context Builder
Assembles structured context for the LLM from portfolio + market + analytics.
"""
from typing import Dict, List


def build_llm_context(
    portfolio_metrics: Dict,
    market_signals: Dict = None,
    thresholds: Dict = None,
) -> Dict:
    """Builds a compact, structured context for the LLM layer."""
    if thresholds is None:
        thresholds = {"sector": 45, "top3": 65, "stock": 30}

    alerts = []
    if portfolio_metrics.get("sector_allocation"):
        top = portfolio_metrics["sector_allocation"][0]
        if top["allocation"] > thresholds["sector"]:
            alerts.append({
                "type": "sector_concentration",
                "metric": f"sector_pct={top['allocation']:.2f}",
                "limit": thresholds["sector"],
            })

    if portfolio_metrics.get("top3_concentration", 0) > thresholds["top3"]:
        alerts.append({
            "type": "top3_concentration",
            "metric": f"top3_pct={portfolio_metrics['top3_concentration']:.2f}",
            "limit": thresholds["top3"],
        })

    return {
        "portfolio": {
            "total_value": portfolio_metrics.get("total_value"),
            "pnl": portfolio_metrics.get("pnl"),
            "hhi": portfolio_metrics.get("hhi"),
            "top3_concentration": portfolio_metrics.get("top3_concentration"),
            "sector_allocation": portfolio_metrics.get("sector_allocation"),
        },
        "market_signals": market_signals or {},
        "alerts": alerts,
        "thresholds": thresholds,
        "data_freshness": "fresh",
    }
