from abc import ABC, abstractmethod


class Encrypter(ABC):
    @abstractmethod
    def encrypt(self, plaintext: str) -> str:
        pass
