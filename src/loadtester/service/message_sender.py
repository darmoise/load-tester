import json
import time
import random
from kafka import KafkaProducer

def create_producer(bootstrap_servers: str) -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

def send_messages(producer, topic: str, messages: list[str], rate: int, duration: int) -> int:
    interval = 1.0 / rate
    end = time.time() + duration
    sent = 0

    while time.time() < end:
        msg = messages[sent]
        producer.send(topic, msg)
        sent += 1
        time.sleep(interval)

    producer.flush()

    return sent
