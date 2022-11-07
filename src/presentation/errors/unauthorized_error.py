class UnauthorizedError(Exception):
    def __init__(self) -> None:
        super().__init__("Unauthorized")
        self.name = "UnauthorizedError"
