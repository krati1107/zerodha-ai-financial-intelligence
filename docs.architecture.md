# Architecture Overview

## Workflow
1. **Input Layer:** User uploads portfolio CSV or selects sample portfolio.
2. **Data Fetch:** Backend fetches market data, news, and corporate actions via APIs.
3. **MCP Unification:** Tools are exposed via MCP server (get_portfolio, get_prices, run_risk_analysis).
4. **Analytics Engine:** Computes HHI, sector concentration, top 3 holdings, P&L drivers.
5. **LLM Analysis:** Gemini API generates explanations using only structured analytics data.
6. **Validation Layer:** Checks for unsupported claims, banned words (buy/sell), and disclaimer presence.
7. **Recommendation Engine:** Generates reviewable cards with rationale, confidence, and metrics.
8. **Dashboards:** Investor view, Operations dashboard, Compliance review panel.

## Tech Stack
- Frontend: HTML/CSS/JS (Prototype), Next.js (Future)
- Backend: FastAPI, Python, Pandas
- AI: Gemini API, LangChain (Future)
- MCP: Custom Python MCP Server
- Database: SQLite (Current), PostgreSQL (Future)
- Deployment: Vercel (Frontend), Render (Backend)
