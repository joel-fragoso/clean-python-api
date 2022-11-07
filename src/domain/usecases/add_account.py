from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AddAccountParams:
    name: str
    email: str
    password: str


class AddAccount(ABC):
    @abstractmethod
    def add(self, account: AddAccountParams) -> bool:
        pass
