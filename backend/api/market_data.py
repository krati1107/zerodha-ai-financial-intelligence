"""
Market Data API
Fetches market quotes, indices, and sector movement signals.
"""
from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/api/market", tags=["Market Data"])

# Sample market data (in production, this comes from Kite Connect API)
SAMPLE_QUOTES = {
    "RELIANCE": {"ltp": 2550, "change_pct": 0.6, "sector": "Energy"},
    "TCS": {"ltp": 3400, "change_pct": -0.9, "sector": "IT"},
    "HDFCBANK": {"ltp": 1650, "change_pct": 0.4, "sector": "Financials"},
    "INFY": {"ltp": 1450, "change_pct": 0.3, "sector": "IT"},
    "ITC": {"ltp": 430, "change_pct": 0.2, "sector": "FMCG"},
}


@router.get("/quote/{symbol}")
def get_quote(symbol: str):
    """Returns latest price for a symbol."""
    symbol = symbol.upper()
    if symbol in SAMPLE_QUOTES:
        return {
            "symbol": symbol,
            "data": SAMPLE_QUOTES[symbol],
            "freshness": datetime.now().isoformat(),
            "source": "market_api",
        }
    return {"symbol": symbol, "error": "Symbol not found", "freshness": None}


@router.post("/refresh")
def refresh_market_data():
    """Triggers a market data refresh job."""
    return {
        "status": "success",
        "message": "Market data refresh queued",
        "timestamp": datetime.now().isoformat(),
    }
