from validators import email as is_email

from src.validation.protocols import EmailValidator


class EmailValidatorAdapter(EmailValidator):
    def is_valid(self, email: str) -> bool:
        return is_email(email)  # type: ignore
