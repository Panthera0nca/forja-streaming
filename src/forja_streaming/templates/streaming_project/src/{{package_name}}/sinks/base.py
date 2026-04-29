"""Sink Protocol — persiste eventos procesados en storage."""
from __future__ import annotations

from typing import Any, Protocol


class Sink(Protocol):
    """Un Sink escribe eventos procesados a un destino final.

    Destinos típicos: Postgres, Delta Lake, archivo, otro topic Kafka.
    """

    def write(self, event: Any) -> None:
        """Persiste un evento procesado."""
        ...

    def flush(self) -> None:
        """Fuerza escritura de eventos en buffer (si aplica)."""
        ...
