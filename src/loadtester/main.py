from loadtester.config.config import load_config
from loadtester.enums.error_code import ErrorCode
from loadtester.errors.common_error import CommonError
from loadtester.service.message_loader import load_messages
from loadtester.service.message_sender import create_producer, send_messages
from loadtester.config.log import setup_logging
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
)

def main():
    cfg = load_config()
    setup_logging(cfg)

    logger = logging.getLogger(__name__)
    logger.info("Configuration loaded")

    kafka_cfg = cfg.kafka
    load_cfg = cfg.load_tester

    messages = load_messages(load_cfg.message_folder)
    if not messages:
        raise CommonError(ErrorCode.EMPTY_MESSAGE_LIST)

    producer = create_producer(kafka_cfg.bootstrap_servers)
    count = send_messages(
        producer=producer,
        topic=kafka_cfg.topic,
        messages=messages,
        rate_start=load_cfg.rate_start,
        rate_step=load_cfg.rate_step,
        step_period=load_cfg.step_period,
        total_duration=load_cfg.duration_seconds
    )
    print(f"Sent {count} messages.")

if __name__ == "__main__":
    main()
