from __future__ import annotations

from datetime import date
import typer
from rich.console import Console

from a365kit_cli.utils.project_context import load_context
from a365kit_cli.utils.renderer import render_template

console = Console()


def mcp_allowlist(
    owner: str = typer.Option("", help="Document owner"),
    server_1: str = typer.Option("TBD", help="MCP server name/url"),
):
    ctx = load_context()
    template_path = ctx.root / ".a365kit" / "templates" / "mcp-allowlist.md"

    today = date.today().isoformat()
    data = {
        "document_id": "ARC-003-MCP-ALLOWLIST-v0.1",
        "title": "MCP Tool Allowlist",
        "owner": owner or "TBD",
        "reviewers": "TBD",
        "approvers": "TBD",
        "created_date": today,
        "updated_date": today,
        "version": "0.1",
        "server_1": server_1,
        "server_1_purpose": "TBD",
        "server_1_tools": "TBD",
        "server_1_scope": "TBD",
    }

    content = render_template(template_path, data)
    out = ctx.docs_dir / "ARC-003-MCP-ALLOWLIST.md"
    out.write_text(content, encoding="utf-8")
    console.print(f"✅ Wrote {out}")
