from dataclasses import dataclass
from typing import Optional

from src.domain.usecases import LoadAccountByToken
from src.presentation.errors import AccessDeniedError
from src.presentation.helpers import forbidden, ok, server_error
from src.presentation.protocols import HttpResponse, Middleware


@dataclass
class AuthMiddlewareRequest:
    access_token: Optional[str]


class AuthMiddleware(Middleware):
    def __init__(
        self, load_account_by_token: LoadAccountByToken, role: Optional[str]
    ) -> None:
        self.__load_account_by_token = load_account_by_token
        self.__role = role

    def handle(self, http_request: AuthMiddlewareRequest) -> HttpResponse:
        try:
            access_token = http_request.access_token
            if access_token:
                account = self.__load_account_by_token.load(access_token, self.__role)
                if account:
                    return ok({"account_id": account.id})
            return forbidden(AccessDeniedError())
        except Exception:
            return server_error()
