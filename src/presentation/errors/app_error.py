import typing as t


class AppError(Exception):
    code: t.Optional[int] = None
    description: t.Optional[str] = None

    def __init__(self, description: t.Optional[str] = None) -> None:
        super().__init__()
        if description is not None:
            self.description = description

    def __str__(self) -> str:
        code = self.code if self.code is not None else "???"
        return f"{code}: {self.description}"

    def __repr__(self) -> str:
        code = self.code if self.code is not None else "???"
        return f"<{type(self).__name__} '{code}'>"
