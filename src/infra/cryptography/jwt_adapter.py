from datetime import datetime, timedelta
from time import mktime

from jwt import decode, encode

from src.data.protocols.cryptography import Decrypter, Encrypter


class JwtAdapter(Encrypter, Decrypter):
    def __init__(self, secret: str) -> None:
        self.__secret = secret

    def encrypt(self, plaintext: str) -> str:
        expiration = datetime.now() + timedelta(days=1)
        payload = {"sub": plaintext, "exp": mktime(expiration.timetuple())}
        return encode(payload, self.__secret, "HS256")

    def decrypt(self, ciphertext: str) -> str:
        test = decode(ciphertext, self.__secret, ["HS256"])
        print(test)
        exit()
        return test
