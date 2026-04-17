"""a365kit CLI entry point."""
from __future__ import annotations

import typer

from a365kit_cli.commands import (
    init,
    blueprint,
    identity,
    mcp_allowlist,
    observability,
    threatmodel,
    eval_plan,
    setup,
)

app = typer.Typer(
    name="a365kit",
    help="Governance-first companion CLI for Microsoft Agent 365.",
    no_args_is_help=True,
    add_completion=False,
)

app.command("init")(init.run)
app.command("blueprint")(blueprint.run)
app.command("identity")(identity.run)
app.command("mcp-allowlist")(mcp_allowlist.run)
app.command("observability")(observability.run)
app.command("threatmodel")(threatmodel.run)
app.command("eval-plan")(eval_plan.run)
app.command("setup")(setup.run)


if __name__ == "__main__":  # pragma: no cover
    app()
