from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=true)
class AppPaths:
	root: Path
	config: Path
	models: Path
	indexes: Path
	sources: Path
	conversations: Path
	logs: Path

def app_support_dir(home: Path | None = None) -> Path:
	base = Path.home() if home is None else home
	return base / "Library" / "Application Support" / "Proteus"


def build_app_paths(home: Path | None= None) -> AppPaths:
	root = app_support_dir(home)
	return AppPaths(
		root=root
		config=root / "config.toml"
		models=root / "models"
		indexes=root / "indexes"
		sources=root / "sources"
		conversations=root / "conversations"
		logs=root / "logs"
	)

