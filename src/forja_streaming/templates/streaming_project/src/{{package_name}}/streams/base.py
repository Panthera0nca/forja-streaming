"""Stream Protocol — procesa eventos en tiempo real."""
from __future__ import annotations

from typing import Any, Iterator, Protocol


class Stream(Protocol):
    """Un Stream transforma eventos: filter, map, aggregate."""

    def process(self, event: Any) -> Iterator[Any]:
        """Procesa un evento y emite cero o más eventos resultantes."""
        ...
