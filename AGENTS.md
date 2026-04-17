# AGENTS.md

This file tells coding agents (Copilot, Cursor, Claude, etc.) and humans how to work in this repo.

## Project
- PyPI: `agent365-kit` | CLI: `a365kit` | Repo: `agent365-governance-kit`
- Python 3.10+, hatchling build backend
- License: MIT

## Layout
- `src/a365kit_cli/` — Typer CLI. One module per subcommand in `commands/`.
- `.a365kit/templates/` — Jinja2 markdown templates (PUBLIC classification).
- `samples/projects/` — worked examples of rendered output.
- `tests/` — smoke tests with pytest.

## Conventions
- Generated artifacts are markdown with a Document Control header (classification, owner, version).
- Templates use Jinja2 (`{{ var }}`), rendered via `utils/renderer.py`.
- CLI subcommands register a `typer.Typer` sub-app from `commands/<name>.py`.
- Keep samples fictional (Contoso etc.). Never embed real customer data.

## Dev loop
```bash
pip install -e .
a365kit --help
pytest -q
```

## Safety rules for agents
- Do not add subprocess calls that bypass `utils/a365_wrapper.py` for Agent 365 CLI interaction.
- Do not log secrets, tokens, or tenant IDs. Redact via `utils/project_context.py`.
- Do not commit generated `a365.generated.config.json` or any file under `.a365/`.
- Do not add network-dependent tests to the default pytest run.

## Commit style
- Conventional commits (`feat:`, `fix:`, `docs:`, `chore:`).
- One logical change per commit.
