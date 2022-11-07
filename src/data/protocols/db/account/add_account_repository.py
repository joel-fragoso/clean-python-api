from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.domain.usecases import AddAccountParams


@dataclass
class AddAccountRepositoryParams(AddAccountParams):
    pass


class AddAccountRepository(ABC):
    @abstractmethod
    def add(self, data: AddAccountRepositoryParams) -> bool:
        pass
