from typing import Optional

from src.data.protocols.cryptography import Decrypter
from src.data.protocols.db.account import LoadAccountByTokenRepository
from src.domain.usecases import LoadAccountByToken, LoadAccountByTokenResult


class DbLoadAccountByToken(LoadAccountByToken):
    def __init__(
        self,
        decrypter: Decrypter,
        load_account_by_token_repository: LoadAccountByTokenRepository,
    ) -> None:
        self.__decrypter = decrypter
        self.__load_account_by_token_repository = load_account_by_token_repository

    def load(
        self, access_token: str, role: Optional[str]
    ) -> Optional[LoadAccountByTokenResult]:
        token: str = ""
        try:
            token = self.__decrypter.decrypt(access_token)
        except:
            return None
        if token:
            account = self.__load_account_by_token_repository.load_by_token(
                access_token, role
            )
            if account:
                return account
        return None
