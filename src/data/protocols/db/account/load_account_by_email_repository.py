from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class LoadAccountByEmailRepositoryResult:
    id: str
    name: str
    password: str


class LoadAccountByEmailRepository(ABC):
    @abstractmethod
    def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult:
        pass
