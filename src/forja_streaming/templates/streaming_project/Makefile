.PHONY: kafka kafka-down kafka-ui stream test lint fmt clean

kafka:
	docker compose up -d

kafka-down:
	docker compose down

kafka-ui:
	@echo "Kafka UI en http://localhost:8080"
	@open http://localhost:8080 2>/dev/null || xdg-open http://localhost:8080 2>/dev/null || true

stream:
	python -m {{ package_name }}.pipelines.stream_pipeline

test:
	pytest -v

lint:
	ruff check src tests

fmt:
	ruff format src tests

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
