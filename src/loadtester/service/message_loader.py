import json
import os

def load_messages(folder: str) -> list[str]:
    messages = []
    for name in os.listdir(folder):
        if name.endswith(".json"):
            path = os.path.join(folder, name)
            try:
                with open(path, "r") as f:
                    messages.append(json.load(f))
            except Exception as e:
                raise
    return messages
