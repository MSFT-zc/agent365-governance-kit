# agent365-governance-kit

> Governance-first blueprints, MCP allowlists, and OpenTelemetry observability templates for **Microsoft Agent 365**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
![Status](https://img.shields.io/badge/status-v0.1--alpha-orange)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

`agent365-governance-kit` is a public, governance-first companion to the Microsoft Agent 365 SDK/CLI. It documents the decisions around it: agent identity, blueprints, governed MCP tool allowlists, OTel observability, threat models, and evaluation plans. It then optionally shells out to the Agent 365 CLI (`a365 setup`) to provision the control-plane pieces.

## Why this exists

Microsoft Agent 365 is a control plane for agents (identity, governance, MCP, OTel). This kit gives you:

- Opinionated markdown templates for 6 governance artifacts
- A tiny CLI (`a365kit`) that renders those templates per-project
- A safe wrapper around `a365 setup all` (with `--skip-infrastructure` passthrough)
- A worked sample project under `samples/projects/001-contoso-hr-agent/`

## Install

```bash
pip install -e .
a365kit --help
```

PyPI name: **`agent365-kit`**. Console script: **`a365kit`**.

## Quickstart

```bash
a365kit init contoso-hr-agent
cd contoso-hr-agent

a365kit blueprint      --agent-name contoso-hr-agent --purpose "HR policy Q&A" --owner "Zen"
a365kit identity       --owner "Zen"
a365kit mcp-allowlist  --owner "Zen" --server-1 "TBD"
a365kit observability  --owner "Zen"
a365kit threatmodel    --agent-name contoso-hr-agent --owner "Zen"
a365kit eval-plan      --owner "Zen"

a365kit setup                       # runs: a365 setup all
a365kit setup --skip-infrastructure # runs: a365 setup all --skip-infrastructure
```

## Commands

| Command | Output |
|---|---|
| `a365kit init <name>` | `./<name>/a365kit.json`, `docs/` |
| `a365kit blueprint` | `docs/ARC-001-BLUEPRINT.md` |
| `a365kit identity` | `docs/ARC-002-IDENTITY.md` |
| `a365kit mcp-allowlist` | `docs/ARC-003-MCP-ALLOWLIST.md` |
| `a365kit observability` | `docs/ARC-004-OBSERVABILITY.md` |
| `a365kit threatmodel` | `docs/ARC-005-THREATMODEL.md` |
| `a365kit eval-plan` | `docs/ARC-006-EVAL-PLAN.md` |
| `a365kit setup` | wrapper around `a365 setup all` |

## Repo layout

```
agent365-kit/
├── src/a365kit_cli/
│   ├── commands/
│   └── utils/
├── .a365kit/templates/
├── samples/projects/001-contoso-hr-agent/
└── tests/
```

## References

- Microsoft Agent 365 SDK Overview
- Agent 365 SDK and CLI
- `a365 setup` command reference

## Status

**v0.1-alpha** — CLI skeleton, templates, sample project, and `a365 setup` wrapper. No internal MSFT material is embedded.

## License

MIT © 2026 Zen Chan
