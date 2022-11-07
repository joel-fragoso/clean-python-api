from dataclasses import dataclass

from src.domain.usecases import (
    AddAccount,
    AddAccountParams,
    Authentication,
    AuthenticationParams,
)
from src.presentation.errors import EmailInUseError
from src.presentation.helpers import bad_request, forbidden, ok, server_error
from src.presentation.protocols import Controller, HttpResponse, Validation


@dataclass
class SignUpControllerRequest:
    name: str
    email: str
    password: str
    password_confirmation: str


class SignUpController(Controller):
    def __init__(
        self,
        add_account: AddAccount,
        validation: Validation,
        authentication: Authentication,
    ) -> None:
        self.__add_account = add_account
        self.__validation = validation
        self.__authentication = authentication

    def handle(self, http_request: SignUpControllerRequest) -> HttpResponse:
        try:
            error = self.__validation.validate(http_request)
            if error:
                return bad_request(error)
            name = http_request["name"]
            email = http_request["email"]
            password = http_request["password"]
            is_valid = self.__add_account.add(AddAccountParams(name, email, password))
            if not is_valid:
                return forbidden(EmailInUseError())
            authentication_model = self.__authentication.auth(
                AuthenticationParams(email, password)
            )
            return ok(authentication_model)
        except Exception:
            return server_error()
