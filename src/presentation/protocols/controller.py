from abc import ABC, abstractmethod
from typing import Any

from .http import HttpResponse


class Controller(ABC):
    @abstractmethod
    def handle(self, http_request: Any) -> HttpResponse:
        pass
