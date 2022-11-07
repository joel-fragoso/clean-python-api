import typing as t
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AddAccountRepositoryParams:
    id: str
    name: str
    email: str
    password: str

    def to_dict(self) -> t.Dict[str, t.Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }


class AddAccountRepository(ABC):
    @abstractmethod
    def add(self, data: AddAccountRepositoryParams) -> bool:
        pass
