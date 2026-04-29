"""Producer Protocol — publica eventos a un Kafka topic."""
from __future__ import annotations

from typing import Any, Protocol


class Producer(Protocol):
    """Un Producer serializa y envía eventos a Kafka.

    No transforma ni procesa — solo publica.
    """

    topic: str

    def produce(self, event: Any) -> None:
        """Serializa el evento y lo envía al topic."""
        ...

    def flush(self) -> None:
        """Espera a que todos los mensajes pendientes sean entregados."""
        ...
