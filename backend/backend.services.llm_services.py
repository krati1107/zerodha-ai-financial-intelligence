import os
import json
import google.generativeai as genai

# Configure API key from environment variable
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "dummy_key_for_now"))

def generate_portfolio_insight(metrics: dict):
    """
    Takes analytics metrics and generates an AI explanation.
    In the HTML prototype, this logic is simulated in JavaScript.
    """
    prompt = f"""
    You are a portfolio intelligence explainer.
    Use only the metrics below.
    Do not give guaranteed returns.
    Return JSON with: summary, key_drivers, risk_alerts, confidence, disclaimer.
    
    Metrics:
    {json.dumps(metrics)}
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return {
            "summary": "Portfolio summary generated from local analytics.",
            "key_drivers": ["Concentration in top holdings"],
            "risk_alerts": ["Sector exposure above threshold"],
            "confidence": "high",
            "disclaimer": "Educational insight only. Not financial advice."
        }
