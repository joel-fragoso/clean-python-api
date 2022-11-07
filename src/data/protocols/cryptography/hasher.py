from abc import ABC, abstractmethod


class Hasher(ABC):
    @abstractmethod
    def hash(self, plaintext: str) -> str:
        pass
