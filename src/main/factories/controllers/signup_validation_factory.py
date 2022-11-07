from src.infra.validators import EmailValidatorAdapter
from src.presentation.protocols import Validation
from src.validation.validators import (
    CompareFieldsValidation,
    EmailValidation,
    RequiredFieldValidation,
    ValidationComposite,
)


def make_signup_validation() -> ValidationComposite:
    validations: list[Validation] = []
    for field in ["name", "email", "password", "password_confirmation"]:
        validations.append(RequiredFieldValidation(field))
    validations.append(CompareFieldsValidation("password", "password_confirmation"))
    validations.append(EmailValidation("email", EmailValidatorAdapter()))
    return ValidationComposite(validations)
