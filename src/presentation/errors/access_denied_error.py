class AccessDeniedError(Exception):
    def __init__(self) -> None:
        super().__init__("Access denied")
        self.name = "AccessDeniedError"
