from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .http import HttpResponse

T = TypeVar("T")


class Middleware(ABC, Generic[T]):
    @abstractmethod
    def handle(self, http_request: T) -> HttpResponse:
        pass
