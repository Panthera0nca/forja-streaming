# forja-streaming

Plugin de [forja](https://pypi.org/project/forja/) que agrega la arquitectura **streaming** con Apache Kafka.

```bash
pip install forja forja-streaming
dfg init mi_proyecto --arch streaming
```

## Stack

- **Apache Kafka** (KRaft, sin Zookeeper) — broker de mensajes
- **confluent-kafka** — cliente Python oficial de Confluent
- **Pydantic** — schemas de eventos tipados
- **Kafka UI** — interfaz web para inspeccionar topics (http://localhost:8080)

## Arquitectura generada

```
src/<proyecto>/
├── producers/          # publican eventos a Kafka topics
├── consumers/          # consumen eventos de Kafka topics
├── streams/            # filtran y transforman eventos
├── sinks/              # persisten eventos procesados
├── schemas/            # modelos Pydantic de eventos
└── pipelines/
    └── stream_pipeline.py  # consumer → stream → sink
```

## Arranque rápido

```bash
docker compose up -d        # Kafka + Kafka UI
pip install -e ".[dev]"
cp .env.example .env
dfg run stream_pipeline     # iniciar el consumer
```

Kafka UI disponible en **http://localhost:8080**

## Integración con forja-lakehouse

El `pyproject.toml` generado incluye un optional `[lakehouse]` para escribir
eventos procesados directamente a Delta Lake:

```bash
pip install -e ".[lakehouse]"
```

## Licencia

MIT
