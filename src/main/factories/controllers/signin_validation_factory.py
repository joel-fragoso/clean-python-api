from src.infra.validators import EmailValidatorAdapter
from src.presentation.protocols import Validation
from src.validation.validators import (
    EmailValidation,
    RequiredFieldValidation,
    ValidationComposite,
)


def make_signin_validation() -> ValidationComposite:
    validations: list[Validation] = []
    for field in ["email", "password"]:
        validations.append(RequiredFieldValidation(field))
    validations.append(EmailValidation("email", EmailValidatorAdapter()))
    return ValidationComposite(validations)
