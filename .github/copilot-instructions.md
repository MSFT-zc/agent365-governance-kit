# GitHub Copilot coding-agent instructions

This file is read by GitHub Copilot (chat, code review, and coding-agent PRs) when operating in this repo. It complements `AGENTS.md`. If they disagree, `AGENTS.md` wins.

## Project snapshot
- **Name**: `agent365-kit` (PyPI) / `a365kit` (CLI) / `agent365-governance-kit` (repo)
- **Purpose**: governance-first companion to Microsoft Agent 365 — blueprints, MCP allowlists, OTel, threat models, eval plans.
- **Language**: Python 3.10+
- **Frameworks**: Typer (CLI), Jinja2 (templates), Rich (output), pytest (tests), hatchling (build)

## What to do
- Prefer small, reviewable PRs. One logical change per PR.
- Use **conventional commit** prefixes: `feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`.
- Add or update tests in `tests/` for every behavior change.
- Keep public template output PUBLIC-safe: no real tenant IDs, customer names, or internal-only Microsoft material.
- When adding a new CLI subcommand:
  1. Create `src/a365kit_cli/commands/<name>.py` exporting a `typer.Typer` app.
  2. Register it in `src/a365kit_cli/main.py`.
  3. If it emits an artifact, add a matching Jinja2 template under `.a365kit/templates/<name>.md`.
  4. Add a smoke test in `tests/test_smoke.py`.
- When adding a new template, include the standard **Document Control** header block.

## What not to do
- Do **not** run `a365` (Agent 365 CLI) directly from agent code; always route through `src/a365kit_cli/utils/a365_wrapper.py`.
- Do **not** log secrets, tokens, tenant IDs, subscription IDs, or user emails. Redact via `utils/project_context.py`.
- Do **not** commit generated artifacts from `a365 setup` (e.g., `a365.generated.config.json`, anything under `.a365/`).
- Do **not** add network calls to default tests. If needed, mark with `@pytest.mark.integration` and exclude from CI default run.
- Do **not** introduce new runtime dependencies without updating `pyproject.toml` and justifying in the PR body.
- Do **not** widen licensing beyond MIT.
- Do **not** scrape or embed internal Microsoft Learn content; link to the public page instead.

## Style
- Format with `black` defaults (88 cols).
- Type hints on all public functions; `mypy --strict` intent (not yet enforced).
- Docstrings: Google style, 1-line summary then optional details.
- Prefer `pathlib.Path` over `os.path`.
- Prefer f-strings over `.format()` or `%`.

## PR checklist for Copilot
- [ ] Title uses conventional commit prefix.
- [ ] `pytest -q` passes locally.
- [ ] `a365kit --help` still renders without import errors.
- [ ] No secrets, tenant IDs, or internal links in diff.
- [ ] README/AGENTS.md updated if the user-facing contract changed.
- [ ] Template changes ship with a matching sample render in `samples/projects/`.

## Review behavior
- When reviewing a PR, flag any violation above as **request changes**.
- Suggest fixes using ```` ```suggestion ```` blocks where possible.
- Batch inline comments via "Start a review" — do not spam single comments.
