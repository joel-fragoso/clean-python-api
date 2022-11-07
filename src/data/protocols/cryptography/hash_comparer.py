from abc import ABC, abstractmethod


class HashComparer(ABC):
    @abstractmethod
    def compare(self, plaintext: str, digest: str) -> bool:
        pass
