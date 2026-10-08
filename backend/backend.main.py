"""
Zerodha AI Financial Intelligence Platform
Main FastAPI Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.portfolio_analysis import router as portfolio_router
from api.market_data import router as market_router
from api.insights import router as insights_router
from api.audit_logs import router as audit_router

app = FastAPI(
    title="Zerodha AI Financial Intelligence Platform",
    description="Portfolio insights, risk alerts, and explainable recommendations.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(portfolio_router)
app.include_router(market_router)
app.include_router(insights_router)
app.include_router(audit_router)


@app.get("/")
def root():
    return {
        "service": "Zerodha AI Financial Intelligence Platform",
        "status": "running",
        "version": "1.0.0",
        "endpoints": [
            "/health",
            "/api/portfolio/analysis",
            "/api/market/quote/{symbol}",
            "/api/insights/generate",
            "/api/audit/",
        ],
    }


@app.get("/health")
def health():
    return {"status": "ok", "service": "zerodha-ai-backend"}
