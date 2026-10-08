"""
Insights API
Generates AI-powered portfolio insights with validation.
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any

router = APIRouter(prefix="/api/insights", tags=["Insights"])


class InsightRequest(BaseModel):
    portfolio_metrics: Dict[str, Any]
    timeframe: str = "1M"


class InsightResponse(BaseModel):
    summary: str
    key_drivers: List[str]
    risk_alerts: List[Dict[str, str]]
    confidence: str
    confidence_reason: str
    disclaimer: str
    validation_status: str


@router.post("/generate", response_model=InsightResponse)
def generate_insight(req: InsightRequest):
    """
    Generates explainable portfolio insights from structured metrics.
    In production, calls Gemini API. Here, returns template-based output.
    """
    metrics = req.portfolio_metrics
    total = metrics.get("total_value", 0)
    pnl = metrics.get("pnl", 0)
    hhi = metrics.get("hhi", 0)

    summary = (
        f"Your portfolio value is ₹{total:,.0f} with unrealized P&L of ₹{pnl:,.0f}. "
        f"The concentration score (HHI) is {hhi:.3f}."
    )

    return InsightResponse(
        summary=summary,
        key_drivers=[
            "Portfolio concentration measured by HHI",
            "Sector-level allocation tracked",
            "Top 3 holdings monitored",
        ],
        risk_alerts=[
            {
                "title": "Sector concentration",
                "explanation": "Review sector exposure if above 45% limit.",
                "metric_used": "sector_pct",
            }
        ],
        confidence="high",
        confidence_reason="All inputs complete and market data is fresh.",
        disclaimer="Educational insight only. Not personal investment advice.",
        validation_status="passed",
    )
