# 🌙 moonclaw-actions-factory

> Production-grade GitHub Actions automation factory for agentic software development

## Stack

- **GitHub Actions** — orchestration layer
- **Debian 13 Trixie self-hosted runner** — execution layer
- **Redis + BullMQ** — queue layer  
- **SQLite WAL** — state layer
- **FastAPI** — API orchestration
- **FastMCP** — agent tools
- **Firecrawl** — web scraping + KB generation
- **Python CLI** — interactive control interface (`cli/moonclaw_cli.py`)
- **`@moonclaw` GitHub App** — comment command router

## Quick Start

```bash
cp .env.example .env   # fill in your keys
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install
python cli/moonclaw_cli.py
```

## Workflows

| Workflow | Trigger | Purpose |
|---|---|---|
| `00-comment-router.yml` | `@moonclaw` comment | Route commands |
| `01-job-dispatch.yml` | `workflow_dispatch` | Enqueue + dispatch jobs |
| `job-scrape-agent-harness-primitives-blue-claw.yml` | dispatch | Scrape agent docs |
| `job-failure-triage.yml` | `workflow_run` failure | Auto-triage + issue |

## CLI

```bash
python cli/moonclaw_cli.py
```

## License

MIT — VibeCodingLabs
