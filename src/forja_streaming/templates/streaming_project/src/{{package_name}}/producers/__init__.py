"""Producers: publican eventos a Kafka topics."""
from .base import Producer
from .kafka_producer import BaseKafkaProducer

__all__ = ["Producer", "BaseKafkaProducer"]
