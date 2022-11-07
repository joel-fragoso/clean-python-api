from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class LoadAccountByTokenRepositoryResult:
    id: str


class LoadAccountByTokenRepository(ABC):
    @abstractmethod
    def load_by_token(
        self, token: str, role: Optional[str]
    ) -> Optional[LoadAccountByTokenRepositoryResult]:
        pass
