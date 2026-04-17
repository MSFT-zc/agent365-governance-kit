from __future__ import annotations

from pathlib import Path
import typer
from rich.console import Console

from a365kit_cli.utils.project_context import load_context
from a365kit_cli.utils.a365_wrapper import run_a365_setup

console = Console()


def setup(
    skip_infrastructure: bool = typer.Option(False, help="Pass --skip-infrastructure to a365 setup"),
):
    ctx = load_context()

    console.print("▶ Running: a365 setup all" + (" --skip-infrastructure" if skip_infrastructure else ""))
    result = run_a365_setup(ctx.root, skip_infrastructure=skip_infrastructure)

    if result.returncode != 0:
        console.print("❌ Agent 365 CLI setup failed")
        if result.stdout:
            console.print("--- stdout ---
" + result.stdout)
        if result.stderr:
            console.print("--- stderr ---
" + result.stderr)
        raise typer.Exit(code=result.returncode)

    console.print("✅ Agent 365 CLI setup completed")
    if result.stdout:
        console.print(result.stdout)

    # Informative check for generated config file
    gen = ctx.root / "a365.generated.config.json"
    if gen.exists():
        console.print(f"✅ Found generated config: {gen}")
    else:
        console.print("ℹ No a365.generated.config.json found in project root (CLI may use a different config directory in your version).")
