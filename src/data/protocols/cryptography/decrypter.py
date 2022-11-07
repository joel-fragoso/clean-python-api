from abc import ABC, abstractmethod


class Decrypter(ABC):
    @abstractmethod
    def decrypt(self, ciphertext: str) -> str:
        pass
