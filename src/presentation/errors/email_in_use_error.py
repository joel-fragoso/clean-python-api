class EmailInUseError(Exception):
    def __init__(self) -> None:
        super().__init__("The received email is already in use")
        self.name = "EmailInUseError"
