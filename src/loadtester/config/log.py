import logging

from loadtester.config.props.props import AppProps

def setup_logging(cfg: AppProps):
    log_cfg = cfg.logging
    level_name = log_cfg.level.upper()
    level = getattr(logging, level_name, logging.INFO)
    log_format = log_cfg.format

    logging.basicConfig(
        level=level,
        format=log_format
    )

    logging.getLogger("kafka").setLevel(logging.ERROR)
    logging.getLogger("kafka.conn").setLevel(logging.ERROR)
    logging.getLogger("urllib3").setLevel(logging.ERROR)

    logging.getLogger(__name__).debug("Logger init with level = %s", level_name)

