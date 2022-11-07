from dataclasses import dataclass

from src.domain.usecases import Authentication, AuthenticationParams
from src.presentation.helpers import bad_request, ok, server_error, unauthorized
from src.presentation.protocols import Controller, HttpResponse, Validation


@dataclass
class SignInControllerRequest:
    email: str
    password: str


class SignInController(Controller):
    def __init__(self, authentication: Authentication, validation: Validation) -> None:
        self.__authentication = authentication
        self.__validation = validation

    def handle(self, http_request: SignInControllerRequest) -> HttpResponse:
        try:
            error = self.__validation.validate(http_request)
            if error:
                return bad_request(error)
            authentication_model = self.__authentication.auth(
                AuthenticationParams(http_request.email, http_request.password)
            )
            print(authentication_model)
            exit()
            if not authentication_model:
                return unauthorized()
            return ok(authentication_model)
        except Exception as error:
            return server_error(error)
