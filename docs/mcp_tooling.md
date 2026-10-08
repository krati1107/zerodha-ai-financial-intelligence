# MCP Server Tooling

## Overview
The MCP (Model Context Protocol) server provides governed tool access for the AI workflow. Tools are schema-bound and audited.

## Registered Tools

| Tool | Input Schema | Purpose |
|------|-------------|---------|
| `list_portfolios` | `{}` | Lists available portfolios |
| `get_portfolio` | `{portfolio: string}` | Returns holdings with P&L |
| `get_prices` | `{symbols: string[]}` | Fetches quotes with freshness |
| `get_news` | `{query: string}` | Returns cited news summary |
| `run_risk_analysis` | `{portfolio: string}` | Computes concentration metrics |
| `score_risk` | `{portfolio: string}` | Returns HHI and limit checks |

## Startup
```bash
cd mcp_server
python server.py
