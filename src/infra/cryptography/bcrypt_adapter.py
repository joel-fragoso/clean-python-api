from bcrypt import checkpw, gensalt, hashpw

from src.data.protocols.cryptography import HashComparer, Hasher


class BcryptAdapter(Hasher, HashComparer):
    def __init__(self, salt: int) -> None:
        self.__salt = salt

    def hash(self, plaintext: str) -> str:
        return hashpw(plaintext.encode("utf-8"), gensalt(self.__salt)).decode("utf-8")

    def compare(self, plaintext: str, digest: str) -> bool:
        return checkpw(plaintext.encode("utf-8"), digest.encode("utf-8"))
