from abc import ABC, abstractmethod
from typing import Any


class Validation(ABC):
    @abstractmethod
    def validate(self, input: Any) -> Exception:
        pass
