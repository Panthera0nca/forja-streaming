"""Registro del plugin forja-streaming."""
from __future__ import annotations

from pathlib import Path

TEMPLATES_PATH = Path(__file__).parent / "templates"


def register(registry) -> None:
    registry.add_architecture(
        key="streaming",
        description="Streaming Kafka — producers / streams / sinks / pipelines",
        template_path=TEMPLATES_PATH / "streaming_project",
        _source="forja-streaming",
    )
