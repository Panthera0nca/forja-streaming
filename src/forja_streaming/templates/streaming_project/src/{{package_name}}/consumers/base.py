"""Consumer Protocol — consume eventos de un Kafka topic."""
from __future__ import annotations

from typing import Any, Iterator, Protocol


class Consumer(Protocol):
    """Un Consumer lee eventos de Kafka y los entrega al stream."""

    topics: list[str]

    def __iter__(self) -> Iterator[Any]:
        """Itera sobre los eventos del topic. Bloquea hasta recibir mensajes."""
        ...

    def commit(self) -> None:
        """Confirma el offset del último mensaje procesado."""
        ...

    def close(self) -> None:
        """Cierra la conexión limpiamente."""
        ...
