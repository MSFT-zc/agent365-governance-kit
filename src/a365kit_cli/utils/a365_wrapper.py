from __future__ import annotations

import subprocess
from pathlib import Path


def run_a365_setup(project_root: Path, skip_infrastructure: bool = False) -> subprocess.CompletedProcess:
    cmd = ["a365", "setup", "all"]
    if skip_infrastructure:
        cmd += ["--skip-infrastructure"]

    # Run in project root so generated config files land there.
    return subprocess.run(
        cmd,
        cwd=str(project_root),
        check=False,
        capture_output=True,
        text=True,
    )
