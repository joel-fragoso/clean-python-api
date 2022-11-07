class ServerError(Exception):
    def __init__(self, traceback: str) -> None:
        super().__init__("Internal server error")
        self.name = "ServerError"
        self.traceback = traceback
