Architecture Overview
Workflow
Input Layer: User uploads portfolio CSV or selects sample portfolio.
Data Fetch: Backend fetches market data, news, and corporate actions via APIs.
MCP Unification: Tools are exposed via MCP server (get_portfolio, get_prices, run_risk_analysis).
Analytics Engine: Computes HHI, sector concentration, top 3 holdings, P&L drivers.
LLM Analysis: Gemini API generates explanations using only structured analytics data.
Validation Layer: Checks for unsupported claims, banned words (buy/sell), and disclaimer presence.
Recommendation Engine: Generates reviewable cards with rationale, confidence, and metrics.
Dashboards: Investor view, Operations dashboard, Compliance review panel.
Tech Stack
Frontend: HTML/CSS/JS (Prototype), Next.js (Future)
Backend: FastAPI, Python, Pandas
AI: Gemini API, LangChain (Future)
MCP: Custom Python MCP Server
Database: SQLite (Current), PostgreSQL (Future)
Deployment: Vercel (Frontend), Render (Backend)
