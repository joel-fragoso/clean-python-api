from typing import Any

from src.presentation.protocols import Validation


class ValidationComposite(Validation):
    def __init__(self, validations: list[Validation]) -> None:
        self.__validations = validations

    def validate(self, input: Any) -> Exception:
        for validation in self.__validations:
            error = validation.validate(input)
            if error:
                return error
