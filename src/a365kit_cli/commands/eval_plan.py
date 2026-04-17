from __future__ import annotations

from datetime import date
import typer
from rich.console import Console

from a365kit_cli.utils.project_context import load_context
from a365kit_cli.utils.renderer import render_template

console = Console()


def eval_plan(
    owner: str = typer.Option("", help="Document owner"),
):
    ctx = load_context()
    template_path = ctx.root / ".a365kit" / "templates" / "eval-plan.md"

    today = date.today().isoformat()
    data = {
        "document_id": "ARC-006-EVALPLAN-v0.1",
        "title": "Evaluation Plan (Pre-publish)",
        "owner": owner or "TBD",
        "reviewers": "TBD",
        "approvers": "TBD",
        "created_date": today,
        "updated_date": today,
        "version": "0.1",
    }

    content = render_template(template_path, data)
    out = ctx.docs_dir / "ARC-006-EVAL-PLAN.md"
    out.write_text(content, encoding="utf-8")
    console.print(f"✅ Wrote {out}")
