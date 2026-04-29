"""Consumers: leen eventos de Kafka topics."""
from .base import Consumer
from .kafka_consumer import BaseKafkaConsumer

__all__ = ["Consumer", "BaseKafkaConsumer"]
