Zerodha AI Financial Intelligence Platform
An AI-powered portfolio intelligence platform that transforms portfolio data, market signals, and analytics into explainable insights and recommendations.

🌐 Live Demo
🔗 Open Live Dashboard on Netlify

📹 Demo Video
▶️ Watch the Demo Video on OneDrive

🚀 Project Overview
Zerodha serves investors who hold diversified portfolios but struggle to interpret what is happening across positions, sectors, risk exposure, and market movement. Portfolio screens show numbers — prices, gains, losses — but they do not explain why the portfolio moved, where risk is concentrated, or what the investor should review next.

This platform solves that gap with a governed AI intelligence layer that:

Converts portfolio data into plain-language explanations

Surfaces concentration and sector risk with metrics

Generates reviewable recommendation cards with rationale

Maintains full compliance auditability

🏗️ Architecture
text
Portfolio Input → Data Fetch → MCP Unification → Analytics Engine
    → LLM Analysis → Validation → Recommendation Engine → Dashboards
Technology Stack:

Layer	Technology
Frontend	HTML, CSS, JavaScript (single-page dashboard)
Backend	FastAPI, Python, Pandas, NumPy
Market Data	Alpha Vantage API with graceful fallback
MCP Server	Custom Python tool registry
AI Workflow	Context builder, validation layer, recommendation engine
Deployment	Netlify (frontend)
📸 Screenshots
Overview Dashboard
Real-time KPIs, performance chart vs NIFTY 50, sector allocation donut, top holdings and movers.

https://screenshots/overview.png

Risk Analysis
HHI concentration index, top-3 holdings check, largest sector exposure with color-coded limits.

https://screenshots/risk.png

AI Analyst
Conversational portfolio intelligence with policy guard — never gives buy/sell advice.

https://screenshots/analyst.png

Insights & Recommendations
8-stage AI pipeline with validated summary and explainable recommendation cards.

https://screenshots/insights.png

Compliance Audit
Full audit trail with validation status, model version, reviewer decisions.

https://screenshots/compliance.png

💻 Current Implementation Status
Frontend Prototype (Working): A fully interactive dashboard (frontend/prototype/index.html) built with HTML/CSS/JS. It demonstrates portfolio overview, risk panels, AI Analyst chat, recommendation cards, and compliance/operations dashboards.

Backend API (FastAPI): Modular backend code (backend/main.py) implements portfolio analysis, market data orchestration, insights generation, and audit endpoints.

AI Workflow: Prompt templates, context builder, validation layer, and recommendation engine are implemented in ai_workflows/ and backend/services/.

MCP Server: Tool registry and governed execution logic is set up in mcp_server/.

📂 Repository Structure
text
zerodha-ai-financial-intelligence/
├── frontend/prototype/index.html    # Working dashboard
├── backend/
│   ├── main.py                       # FastAPI app
│   ├── api/                          # API endpoints
│   ├── services/                     # Business logic
│   └── database/schema.sql           # DB schema
├── mcp_server/server.py              # MCP tool registry
├── ai_workflows/                     # Context, validation, recommendations
├── data/sample_portfolios.csv        # Sample data
├── docs/                             # Architecture, API, MCP tooling
└── screenshots/                      # Dashboard screenshots
⚙️ How to Run Locally
Frontend Prototype
Clone the repository

Navigate to frontend/prototype/

Open index.html in a browser

Click "Start with a sample portfolio"

Backend API
bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
API documentation available at http://localhost:8000/docs

🔐 Environment Variables
Copy .env.example to .env and fill in your keys:

text
MARKET_API_KEY=your_alpha_vantage_key
MCP_SERVER_URL=http://localhost:8001
GEMINI_API_KEY=your_gemini_key
DATABASE_URL=sqlite:///./zerodha.db
📡 API Endpoints
Method	Endpoint	Purpose
GET	/health	Health check
POST	/api/portfolio/analysis	Portfolio metrics computation
GET	/api/market/quote/{symbol}	Fetch live quote
POST	/api/market/refresh	Trigger market data refresh
POST	/api/insights/generate	Generate AI insights
POST	/api/audit/log	Store audit log
GET	/api/audit/{job_id}	Retrieve audit trail
📊 Evaluation Approach
The platform is evaluated on:

Criterion	How It Is Measured
Factual Grounding	Every number in AI output is cross-checked against analytics payload
Safety	Banned-language detection (buy/sell/guarantee)
Explainability	Recommendation cards include rationale, metric, source, confidence
Data Freshness	Confidence is lowered when market data is stale
Validation	3-stage check: numbers grounded, no banned words, alert count matches
Fallback Behavior	Graceful degradation when API fails
Test scenarios covered:

Concentrated portfolio → triggers risk alerts

Stale market data → lowers confidence

Unsafe AI output → blocked by validation layer

Missing holdings → handled gracefully

⚠️ Known Limitations
No real-time WebSocket feed — Market data is fetched via Alpha Vantage REST API with 15-min cache

No volatility/drawdown/Sharpe — These require historical price data, not yet connected

Simulated AI in prototype — Frontend uses template-based explanations; production LLM integration is scaffolded

No persistent database in demo — Audit logs stored in-memory; production schema defined in backend/database/schema.sql

Single portfolio per session — Multi-account support out of scope for v1

🚀 Future Improvements
Integrate Kite Connect API for real-time portfolio sync

Add historical price data for volatility, drawdown, Sharpe ratio

Multi-portfolio and multi-user support

Vector memory for reusable financial explanations

Scenario analysis and tax-aware summaries

Advisor-grade workflows

🛡️ Safety and Governance
Validation layer blocks unsupported claims and buy/sell language

All outputs include disclaimers

Audit logs capture model version, prompt version, validation status

Compliance review panel with reviewer decisions

Human-in-the-loop for high-risk recommendations

👤 Author
Made by Krati Shrivastava

GitHub: @krati1107

Role: Sole contributor — Product design, frontend, backend, AI workflows, MCP server, documentation, and testing

This is a solo project. All components were designed and implemented individually by Krati Shrivastava.
