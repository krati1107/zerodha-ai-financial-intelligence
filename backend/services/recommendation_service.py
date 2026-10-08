"""
Recommendation Service
Converts analytics into reviewable recommendation cards.
"""
from typing import List, Dict


def build_recommendation_cards(metrics: dict, thresholds: dict = None) -> List[Dict]:
    """Creates recommendation cards based on portfolio metrics."""
    if thresholds is None:
        thresholds = {"sector": 45, "top3": 65, "stock": 30}

    cards = []

    # Sector concentration
    if metrics["sector_allocation"]:
        top_sector = metrics["sector_allocation"][0]
        if top_sector["allocation"] > thresholds["sector"]:
            cards.append({
                "category": "Risk alert",
                "signal": f"Sector concentration: {top_sector['sector']}",
                "rationale": f"{top_sector['sector']} is {top_sector['allocation']:.2f}% of your portfolio.",
                "metric": f"sector_pct={top_sector['allocation']:.2f}",
                "confidence": 0.9,
                "disclaimer_required": True,
            })

    # Top 3 concentration
    if metrics["top3_concentration"] > thresholds["top3"]:
        cards.append({
            "category": "Risk alert",
            "signal": "Top 3 holdings concentration",
            "rationale": f"Top 3 holdings are {metrics['top3_concentration']:.2f}% of portfolio.",
            "metric": f"top3_pct={metrics['top3_concentration']:.2f}",
            "confidence": 0.9,
            "disclaimer_required": True,
        })

    # Educational
    cards.append({
        "category": "Educational insight",
        "signal": "Understanding your HHI",
        "rationale": "HHI measures concentration. Lower means more diversified.",
        "metric": f"hhi={metrics['hhi']:.3f}",
        "confidence": 0.95,
        "disclaimer_required": False,
    })

    return cards
