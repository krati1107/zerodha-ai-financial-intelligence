SYSTEM_PROMPT = """
You are a portfolio intelligence explainer. 
Use only the provided structured data. 
Never invent numbers. 
Always include a disclaimer that this is educational, not financial advice.
"""

VALIDATION_RULES = {
    "no_buy_sell_words": True,
    "numbers_must_match_analytics": True,
    "disclaimer_required": True,
    "confidence_calibration": True
}

OUTPUT_SCHEMA = {
    "summary": "string",
    "key_drivers": ["string"],
    "risk_alerts": [{"title": "string", "explanation": "string", "metric_used": "string"}],
    "confidence": "high | medium | low",
    "confidence_reason": "string",
    "disclaimer": "string"
}
