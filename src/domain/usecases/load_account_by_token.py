from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class LoadAccountByTokenResult:
    id: str


class LoadAccountByToken(ABC):
    @abstractmethod
    def load(self, access_token: str, role: Optional[str]) -> LoadAccountByTokenResult:
        pass
