from abc import ABC, abstractmethod
from typing import Any

from .http import HttpResponse


class Middleware(ABC):
    @abstractmethod
    def handle(self, http_request: Any) -> HttpResponse:
        pass
