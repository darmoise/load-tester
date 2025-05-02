from loadtester.enums.error_code import ErrorCode

class CommonError(Exception):
    def __init__(self, error_code: ErrorCode):
        self.code = error_code.code
        self.message = error_code.message
        super().__init__(f"[{self.code}] {self.message}")
