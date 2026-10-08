"""
Validation Layer
Ensures AI outputs are safe, grounded, and compliant.
"""
import re
from typing import Dict, List, Tuple

BANNED_PATTERNS = [
    r"\bbuy\b", r"\bsell\b", r"\bhold\b",
    r"guarantee", r"risk[- ]free", r"sure[- ]?(shot|profit)",
    r"will (definitely|surely)",
]

REQUIRED_FIELDS = [
    "summary", "key_drivers", "risk_alerts",
    "confidence", "confidence_reason", "disclaimer",
]

NUMBER_REGEX = re.compile(r"\d+(?:,\d+)*(?:\.\d+)?")


def extract_numbers(obj, store=None) -> set:
    """Recursively extracts numbers from nested structure."""
    if store is None:
        store = set()
    if isinstance(obj, (int, float)):
        if obj == obj:  # not NaN
            store.add(abs(obj))
    elif isinstance(obj, str):
        for m in NUMBER_REGEX.findall(obj):
            store.add(float(m.replace(",", "")))
    elif isinstance(obj, dict):
        for v in obj.values():
            extract_numbers(v, store)
    elif isinstance(obj, (list, tuple)):
        for v in obj:
            extract_numbers(v, store)
    return store


def validate_insight(insight: Dict, analytics: Dict) -> Tuple[bool, List[Dict]]:
    """Validates an AI insight for safety and grounding."""
    checks = []

    # Check required fields
    missing = [f for f in REQUIRED_FIELDS if f not in insight]
    checks.append({
        "name": "required_fields",
        "passed": len(missing) == 0,
        "detail": f"Missing: {missing}" if missing else "All fields present",
    })

    # Check for banned words
    text = " ".join(str(v) for v in insight.values())
    banned = [p for p in BANNED_PATTERNS if re.search(p, text, re.IGNORECASE)]
    checks.append({
        "name": "no_banned_language",
        "passed": len(banned) == 0,
        "detail": f"Found: {banned}" if banned else "No banned wording",
    })

    # Check numbers are grounded
    allowed = extract_numbers(analytics)
    found = extract_numbers(insight.get("summary", ""))
    ungrounded = [n for n in found if not any(abs(n - a) < 0.01 for a in allowed) and n > 5]
    checks.append({
        "name": "numbers_grounded",
        "passed": len(ungrounded) == 0,
        "detail": f"Ungrounded: {ungrounded}" if ungrounded else "All numbers grounded",
    })

    # Check disclaimer
    checks.append({
        "name": "disclaimer_present",
        "passed": bool(insight.get("disclaimer")),
        "detail": "Disclaimer present" if insight.get("disclaimer") else "No disclaimer",
    })

    overall = all(c["passed"] for c in checks)
    return overall, checks
