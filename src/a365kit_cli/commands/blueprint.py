from __future__ import annotations

from datetime import date
from pathlib import Path
import typer
from rich.console import Console

from a365kit_cli.utils.project_context import load_context
from a365kit_cli.utils.renderer import render_template

console = Console()


def blueprint(
    agent_name: str = typer.Option("contoso-agent", help="Agent name"),
    purpose: str = typer.Option("", help="One-line purpose"),
    owner: str = typer.Option("", help="Document owner"),
):
    ctx = load_context()
    template_path = ctx.root / ".a365kit" / "templates" / "blueprint.md"

    today = date.today().isoformat()
    data = {
        "document_id": "ARC-001-BLUEPRINT-v0.1",
        "title": "Agent 365 Blueprint Design",
        "owner": owner or "TBD",
        "reviewers": "TBD",
        "approvers": "TBD",
        "created_date": today,
        "updated_date": today,
        "version": "0.1",
        "agent_name": agent_name,
        "purpose": purpose or "TBD",
        "primary_users": "TBD",
        "channels": "Teams, M365 Copilot (example)",
        "identity_pattern": "Entra-backed Agent Identity (design)",
        "m365_workloads": "Mail, Calendar, SharePoint (example)",
        "approval_model": "Admin consent + AI admin approval (example)",
        "mcp_server_1": "TBD",
        "mcp_server_1_tools": "TBD",
    }

    content = render_template(template_path, data)
    out = ctx.docs_dir / "ARC-001-BLUEPRINT.md"
    out.write_text(content, encoding="utf-8")
    console.print(f"✅ Wrote {out}")
