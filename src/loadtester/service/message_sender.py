import json
import time
import random
from kafka import KafkaProducer
import logging

def create_producer(bootstrap_servers: str) -> KafkaProducer:
    return KafkaProducer(
        bootstrap_servers=bootstrap_servers,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )

def send_messages(
    producer,
    topic: str,
    messages: list[str],
    rate_start: int,
    rate_step: int,
    step_period: int,
    total_duration: int,
) -> int:
    start_time = time.time()
    current_rate = rate_start
    sent = 0
    previous_step = None

    while True:
        now = time.time()
        elapsed = now - start_time

        if elapsed >= total_duration:
            break

        current_step = int(elapsed // step_period)

        current_rate = rate_start + current_step * rate_step
        interval = 1.0 / current_rate if current_rate > 0 else 0.001

        if current_step != previous_step:
            logging.info(f"Step {current_step}: rate changed to {current_rate} msg/sec (new interval: {interval})")
            previous_step = current_step

        msg = random.choice(messages)
        producer.send(topic, msg)
        sent += 1

        logging.debug(f"Sent message with num = {sent} to {topic}")
        time.sleep(interval)

    producer.flush()
    producer.close()
    return sent
