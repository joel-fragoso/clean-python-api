from typing import Optional

from src.data.protocols.cryptography import Encrypter, HashComparer
from src.data.protocols.db.account import (
    LoadAccountByEmailRepository,
    UpdateAccessTokenRepository,
)
from src.domain.usecases import (
    Authentication,
    AuthenticationParams,
    AuthenticationResult,
)


class DbAuthentication(Authentication):
    def __init__(
        self,
        load_account_by_email_repository: LoadAccountByEmailRepository,
        hash_comparer: HashComparer,
        encrypter: Encrypter,
        update_access_token_repository: UpdateAccessTokenRepository,
    ) -> None:
        self.__load_account_by_email_repository = load_account_by_email_repository
        self.__hash_comparer = hash_comparer
        self.__encrypter = encrypter
        self.__update_access_token_repository = update_access_token_repository

    def auth(
        self, authentication_params: AuthenticationParams
    ) -> Optional[AuthenticationResult]:
        print(authentication_params)
        exit()
        account = self.__load_account_by_email_repository.load_by_email(
            authentication_params.email
        )
        if account:
            is_valid = self.__hash_comparer.compare(
                authentication_params.password, account.password
            )
            if is_valid:
                access_token = self.__encrypter.encrypt(account.id)
                self.__update_access_token_repository.update_access_token(
                    account.id, access_token
                )
                return AuthenticationResult(access_token, account.name)
        return None
