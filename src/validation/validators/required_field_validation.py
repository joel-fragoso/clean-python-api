from typing import Any

from src.presentation.errors import MissingParamError
from src.presentation.protocols import Validation


class RequiredFieldValidation(Validation):
    def __init__(self, field_name: str) -> None:
        self.__field_name = field_name

    def validate(self, input: Any):
        if not input[self.__field_name]:
            raise MissingParamError(self.__field_name)
