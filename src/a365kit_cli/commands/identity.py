from __future__ import annotations

from datetime import date
import typer
from rich.console import Console

from a365kit_cli.utils.project_context import load_context
from a365kit_cli.utils.renderer import render_template

console = Console()


def identity(
    owner: str = typer.Option("", help="Document owner"),
):
    ctx = load_context()
    template_path = ctx.root / ".a365kit" / "templates" / "identity.md"

    today = date.today().isoformat()
    data = {
        "document_id": "ARC-002-IDENTITY-v0.1",
        "title": "Agent Identity & Access Plan",
        "owner": owner or "TBD",
        "reviewers": "TBD",
        "approvers": "TBD",
        "created_date": today,
        "updated_date": today,
        "version": "0.1",
        "agent_identity_type": "Entra-backed Agent Identity (design)",
        "tenant_notes": "TBD",
        "blueprint_doc": "docs/ARC-001-BLUEPRINT.md",
    }

    content = render_template(template_path, data)
    out = ctx.docs_dir / "ARC-002-IDENTITY.md"
    out.write_text(content, encoding="utf-8")
    console.print(f"✅ Wrote {out}")
