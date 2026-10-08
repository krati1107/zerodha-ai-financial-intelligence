"""
Recommendation Engine
Converts validated insights into reviewable recommendation cards.
"""
from typing import Dict, List


def generate_cards(insight: Dict, analytics: Dict) -> List[Dict]:
    """Generates categorized recommendation cards."""
    cards = []

    # Risk alerts
    for alert in insight.get("risk_alerts", []):
        cards.append({
            "category": "Risk alert",
            "signal": alert.get("title", "Risk detected"),
            "rationale": alert.get("explanation", ""),
            "metric": alert.get("metric_used", ""),
            "confidence": 0.9,
            "disclaimer_required": True,
        })

    # Review prompts
    for area in insight.get("review_areas", []):
        cards.append({
            "category": "Review prompt",
            "signal": "Suggested review",
            "rationale": area,
            "metric": f"hhi={analytics.get('hhi', 0):.3f}",
            "confidence": 0.85,
            "disclaimer_required": True,
        })

    # Educational
    cards.append({
        "category": "Educational insight",
        "signal": "How HHI works",
        "rationale": "HHI is the sum of squared weights. Lower = more diversified.",
        "metric": f"hhi={analytics.get('hhi', 0):.3f}",
        "confidence": 0.95,
        "disclaimer_required": False,
    })

    return cards
