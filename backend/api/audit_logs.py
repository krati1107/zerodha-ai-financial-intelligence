"""
Audit Logs API
Tracks every AI output for compliance review.
"""
from fastapi import APIRouter
from datetime import datetime
from typing import List, Dict, Any

router = APIRouter(prefix="/api/audit", tags=["Audit"])

# In-memory store (production: PostgreSQL)
AUDIT_STORE: List[Dict[str, Any]] = []


@router.post("/log")
def create_audit_log(entry: Dict[str, Any]):
    """Stores an audit log entry for a generated output."""
    entry["timestamp"] = datetime.now().isoformat()
    entry["id"] = len(AUDIT_STORE) + 1
    AUDIT_STORE.append(entry)
    return {"status": "success", "audit_id": entry["id"]}


@router.get("/{job_id}")
def get_audit_log(job_id: int):
    """Retrieves audit trail for a specific job."""
    for entry in AUDIT_STORE:
        if entry["id"] == job_id:
            return entry
    return {"error": "Audit log not found", "job_id": job_id}


@router.get("/")
def list_audit_logs():
    """Lists all audit logs (for compliance dashboard)."""
    return {"total": len(AUDIT_STORE), "logs": AUDIT_STORE[-20:]}
