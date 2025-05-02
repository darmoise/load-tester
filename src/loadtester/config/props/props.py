from dataclasses import dataclass

@dataclass
class KafkaConfig:
    bootstrap_servers: str
    topic: str

@dataclass
class LoadTesterConfig:
    messages_per_second: int
    duration_seconds: int
    message_folder: str

@dataclass
class AppConfig:
    kafka: KafkaConfig
    load_tester: LoadTesterConfig
