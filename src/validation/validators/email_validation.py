from typing import Any

from src.presentation.errors import InvalidParamError
from src.presentation.protocols import Validation
from src.validation.protocols import EmailValidator


class EmailValidation(Validation):
    def __init__(self, field_name: str, email_validator: EmailValidator) -> None:
        self.__field_name = field_name
        self.__email_validator = email_validator

    def validate(self, input: Any) -> Exception:
        is_valid = self.__email_validator.is_valid(input[self.__field_name])
        if not is_valid:
            return InvalidParamError(self.__field_name)
