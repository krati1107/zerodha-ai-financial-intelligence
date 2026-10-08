# API Documentation

## Base URL
- Local: `http://localhost:8000`
- Production: *(after deploy)*

## Endpoints

### GET /health
Health check endpoint.
**Response:** `{"status": "ok", "service": "zerodha-ai-backend"}`

### POST /api/portfolio/analysis
Computes portfolio metrics.
**Query Params:** `portfolio_id` (optional)
**Response:** Total value, holdings, sector allocation, top movers

### GET /api/market/quote/{symbol}
Fetches latest quote for a symbol.
**Response:** `{"symbol": "TCS", "data": {"ltp": 3400, "change_pct": -0.9}}`

### POST /api/market/refresh
Triggers a market data refresh.

### POST /api/insights/generate
Generates explainable AI insights.
**Body:** `{"portfolio_metrics": {...}, "timeframe": "1M"}`
**Response:** summary, key_drivers, risk_alerts, confidence, disclaimer

### POST /api/audit/log
Stores audit log entry.

### GET /api/audit/{job_id}
Retrieves audit trail for a job.

### GET /api/audit/
Lists all audit logs.

## Error Codes
- 400: Bad request
- 404: Not found
- 500: Server error
