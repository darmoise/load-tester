from enum import Enum

class ErrorCode(Enum):
    UNABLE_TO_READ_MESSAGES = ("UNABLE_TO_READ_MESSAGES", "Unable to read messages")
    EMPTY_MESSAGE_LIST = ("EMPTY_MESSAGE_LIST", "Empty message list")

    def __init__(self, code: str, message: str):
        self._code = code
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def message(self):
        return self._message