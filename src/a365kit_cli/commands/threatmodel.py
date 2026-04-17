from __future__ import annotations

from datetime import date
import typer
from rich.console import Console

from a365kit_cli.utils.project_context import load_context
from a365kit_cli.utils.renderer import render_template

console = Console()


def threatmodel(
    agent_name: str = typer.Option("contoso-agent", help="Agent name"),
    owner: str = typer.Option("", help="Document owner"),
):
    ctx = load_context()
    template_path = ctx.root / ".a365kit" / "templates" / "threatmodel.md"

    today = date.today().isoformat()
    data = {
        "document_id": "ARC-005-THREATMODEL-v0.1",
        "title": "Threat Model",
        "owner": owner or "TBD",
        "reviewers": "TBD",
        "approvers": "TBD",
        "created_date": today,
        "updated_date": today,
        "version": "0.1",
        "agent_name": agent_name,
        "channels": "Teams, M365 Copilot (example)",
    }

    content = render_template(template_path, data)
    out = ctx.docs_dir / "ARC-005-THREATMODEL.md"
    out.write_text(content, encoding="utf-8")
    console.print(f"✅ Wrote {out}")
