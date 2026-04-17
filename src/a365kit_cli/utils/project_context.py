from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

DEFAULT_META = {
  "project_name": "",
  "version": "0.1",
  "artifact_prefix": "ARC",
}

@dataclass
class ProjectContext:
    root: Path
    meta: dict

    @property
    def docs_dir(self) -> Path:
        return self.root / "docs"

    def artifact_path(self, num: int, name: str) -> Path:
        prefix = self.meta.get("artifact_prefix", "ARC")
        return self.docs_dir / f"{prefix}-{num:03d}-{name}.md"


def load_context(cwd: Path | None = None) -> ProjectContext:
    root = (cwd or Path.cwd()).resolve()
    meta_path = root / "a365kit.json"
    if meta_path.exists():
        meta = json.loads(meta_path.read_text(encoding="utf-8"))
    else:
        meta = DEFAULT_META.copy()
    return ProjectContext(root=root, meta=meta)


def save_context(ctx: ProjectContext) -> None:
    (ctx.root / "a365kit.json").write_text(json.dumps(ctx.meta, indent=2), encoding="utf-8")
