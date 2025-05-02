import yaml

from loadtester.config.props.props import AppProps, KafkaProps, LoadTesterProps, \
    LoggerProps

def load_config(path: str = "config.yml") -> AppProps:
    with open(path) as f:
        raw = yaml.safe_load(f)

    return AppProps(
        kafka=KafkaProps(**raw["kafka"]),
        load_tester=LoadTesterProps(**raw["load_tester"]),
        logging=LoggerProps(**raw["logging"])
    )
