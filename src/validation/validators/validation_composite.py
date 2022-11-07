import typing as t

from src.presentation.protocols import Validation


class ValidationComposite(Validation):
    def __init__(self, validations: t.List[Validation]) -> None:
        self.__validations = validations

    def validate(self, input: t.Any):
        for validation in self.__validations:
            error = validation.validate(input)
            if error:
                raise error

    def __str__(self) -> str:
        return f"{self.__validations}"

    def __repr__(self) -> str:
        return f"<{type(self).__name__} {self.__validations}>"
