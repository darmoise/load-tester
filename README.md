# LoadTester

**LoadTester** is a Python-based utility for load testing Apache Kafka by sending predefined JSON messages at configurable rates. It supports progressive load increase and is designed for data stream stress testing and throughput benchmarking.

## Features

- Send JSON messages to Kafka at a configurable rate
- Step-based automatic rate increase (e.g. +10 msg/s every minute)
- Load test messages from a folder of `.json` files
- Fully configurable via `config.yml`
- Structured logging with levels and formats
- Built-in error handling via custom `ErrorCode` enums
- Designed for extensibility and observability (Prometheus-ready)

## Configuration (`config.yml`)

```yaml
kafka:
  bootstrap_servers: 127.0.0.1:9092
  topic: test-topic

load_tester:
  rate_start: 100             # messages per second
  rate_step: 10               # increase step
  step_period: 60             # every 60 seconds
  duration_seconds: 300       # total test duration
  message_folder: messages    # folder with JSON messages

logging:
  level: DEBUG
  format: "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
````

## Running the Load Test
```bash
poetry run python src/loadtester/main.py
```

📦 LoadTester will:

1. Load config from `config.yml`
2. Load messages from the configured folder
3. Connect to Kafka
4. Send messages with step-wise increasing rate
5. Log metrics and progress

## Dependencies

* Python 3.11+
* `kafka-python`
* `PyYAML`
* `poetry` for dependency management