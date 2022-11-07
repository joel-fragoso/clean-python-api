from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class AuthenticationParams:
    email: str
    password: str


@dataclass
class AuthenticationResult:
    access_token: str
    name: str


class Authentication(ABC):
    @abstractmethod
    def auth(
        self, authentication_params: AuthenticationParams
    ) -> Optional[AuthenticationResult]:
        pass
