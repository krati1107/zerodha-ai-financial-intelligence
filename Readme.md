# Zerodha AI Financial Intelligence Platform

## 🚀 Project Overview
An AI-powered portfolio intelligence platform that transforms portfolio data, market signals, and analytics into explainable insights and recommendations.

## 🏗️ Architecture
Portfolio Input -> Data Fetch -> MCP Unification -> Analytics Engine -> LLM Analysis -> Recommendation Engine -> Dashboards


## 🌐 Live Demo
**[🔗 Open Live Dashboard on Netlify](https://amazing-licorice-6b392f.netlify.app)**

## 📹 Demo Video
**[▶️ Watch the Demo Video on OneDrive](https://1drv.ms/f/c/0C3C682A870456A0/IgBuevacCYnxS7JwBxCysJftAaS-32Xre-_z-0u7L0L1oOc?e=pbRy7W)**

---
## 📸 Screenshots

### Overview Dashboard
![Overview](docs/screenshots/overview.png)

### Risk Analysis
![Risk](docs/screenshots/risk.png)

### AI Analyst
![Analyst](docs/screenshots/analyst.png)

### Insights & Recommendations
![Insights](docs/screenshots/insights.png)

### Compliance Audit
![Compliance](docs/screenshots/compliance.png)

## 💻 Current Implementation Status

- **Frontend Prototype (Working):** A fully interactive dashboard (`frontend/prototype/index.html`) built with HTML/CSS/JS. It demonstrates portfolio overview, risk panels, AI Analyst chat, recommendation cards, and compliance/operations dashboards.
- **Backend API (FastAPI):** The backend code (`backend/main.py`) implements portfolio analysis, market data orchestration, and insight generation endpoints.
- **AI Workflow:** Prompt templates, context builder, validation layer, and recommendation engine are implemented in `ai_workflows/` and `backend/services/`.
- **MCP Server:** Tool registry and execution logic are set up in `mcp_server/`.

## ⚙️ How to Run the Frontend Prototype
1. Clone this repository.
2. Navigate to `frontend/prototype/`.
3. Double-click `index.html`.
4. Click on **"Start with a sample portfolio"** to see the full end-to-end UI workflow.

## 📂 Sample Data
Sample portfolio data is provided in the `data/` folder.

## 🛡️ Safety and Governance
The platform includes validation rules to prevent unsupported financial claims, disclaimers on all outputs, and audit logs for compliance review.

---

## 👤 Author

**Made by Krati Shrivastava**

- GitHub: [@krati1107](https://github.com/krati1107)
- Role: Sole contributor — Product design, frontend, backend, AI workflows, MCP server, documentation, and testing

*This is a solo project. All components were designed and implemented individually by Krati Shrivastava.*
