"""
Market Service
Fetches and normalizes market data from Alpha Vantage API.
"""
import os
from datetime import datetime
import httpx
from dotenv import load_dotenv

load_dotenv()

MARKET_API_KEY = os.getenv("MARKET_API_KEY", "")
ALPHA_VANTAGE_URL = "https://www.alphavantage.co/query"


async def fetch_quote(symbol: str) -> dict:
    """
    Fetches latest quote for a symbol from Alpha Vantage.
    Falls back to mocked data if API key is missing or call fails.
    """
    symbol = symbol.upper()

    # Fallback if no API key configured
    if not MARKET_API_KEY:
        return _mocked_quote(symbol, reason="no_api_key")

    try:
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": f"{symbol}.BSE",  # NSE/BSE suffix
            "apikey": MARKET_API_KEY,
        }
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(ALPHA_VANTAGE_URL, params=params)
            data = response.json()

        quote = data.get("Global Quote", {})
        if not quote:
            return _mocked_quote(symbol, reason="no_data")

        return {
            "symbol": symbol,
            "ltp": float(quote.get("05. price", 0)),
            "change_pct": float(quote.get("10. change percent", "0%").rstrip("%")),
            "volume": int(quote.get("06. volume", 0)),
            "freshness": datetime.now().isoformat(),
            "source": "alpha_vantage",
        }
    except Exception as e:
        return _mocked_quote(symbol, reason=f"api_error: {str(e)[:50]}")


def _mocked_quote(symbol: str, reason: str = "unknown") -> dict:
    """Returns mocked data when API unavailable — graceful degradation."""
    return {
        "symbol": symbol,
        "ltp": 1000.0,
        "change_pct": 0.5,
        "volume": 1000000,
        "freshness": datetime.now().isoformat(),
        "source": "mocked_fallback",
        "fallback_reason": reason,
    }


def check_freshness(timestamp: str) -> bool:
    """Returns True if data is less than 15 minutes old."""
    try:
        ts = datetime.fromisoformat(timestamp)
        age = (datetime.now() - ts).total_seconds()
        return age < 900
    except Exception:
        return False
