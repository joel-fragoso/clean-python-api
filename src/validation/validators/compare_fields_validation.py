from typing import Any

from src.presentation.errors import InvalidParamError
from src.presentation.protocols import Validation


class CompareFieldsValidation(Validation):
    def __init__(self, field_name: str, field_to_compare_name: str) -> None:
        self.__field_name = field_name
        self.__field_to_compare_name = field_to_compare_name

    def validate(self, input: Any) -> Exception:
        if input[self.__field_name] != input[self.__field_to_compare_name]:
            return InvalidParamError(self.__field_to_compare_name)
