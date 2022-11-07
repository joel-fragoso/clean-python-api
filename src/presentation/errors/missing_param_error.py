class MissingParamError(Exception):
    def __init__(self, param_name: str) -> None:
        super().__init__(f"Missing param: {param_name}")
        self.name = "MissingParamError"
