"""
Market Service
Fetches and normalizes market data.
"""
from datetime import datetime


def fetch_quote(symbol: str) -> dict:
    """Fetches latest quote for a symbol (mocked)."""
    # In production: uses Kite Connect API or Alpha Vantage
    return {
        "symbol": symbol,
        "ltp": 1000.0,
        "change_pct": 0.5,
        "freshness": datetime.now().isoformat(),
        "source": "mocked_market_api",
    }


def check_freshness(timestamp: str) -> bool:
    """Returns True if data is less than 15 minutes old."""
    try:
        ts = datetime.fromisoformat(timestamp)
        age = (datetime.now() - ts).total_seconds()
        return age < 900
    except Exception:
        return False
