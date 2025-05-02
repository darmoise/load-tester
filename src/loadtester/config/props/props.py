from dataclasses import dataclass

@dataclass
class KafkaProps:
    bootstrap_servers: str
    topic: str

@dataclass
class LoggerProps:
    level: str
    format: str

@dataclass
class LoadTesterProps:
    rate_start: int
    rate_step: int
    step_period: int
    duration_seconds: int
    message_folder: str

@dataclass
class AppProps:
    kafka: KafkaProps
    load_tester: LoadTesterProps
    logging: LoggerProps
