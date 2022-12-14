from typing import TypedDict

from src.domain.usecases import Authentication, AuthenticationParams
from src.presentation.helpers import bad_request, ok, server_error, unauthorized
from src.presentation.protocols import Controller, HttpResponse, Validation


class SignInControllerRequest(TypedDict):
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
                AuthenticationParams(
                    http_request.get("email"), http_request.get("password")
                )
            )
            if not authentication_model:
                return unauthorized()
            return ok(authentication_model)
        except Exception:
            return server_error()
