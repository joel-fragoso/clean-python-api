from src.data.protocols.cryptography import Hasher
from src.data.protocols.db.account import (
    AddAccountRepository,
    CheckAccountByEmailRepository,
)
from src.domain.usecases import AddAccount, AddAccountParams


class DbAddAccount(AddAccount):
    def __init__(
        self,
        hasher: Hasher,
        add_account_repository: AddAccountRepository,
        check_account_by_email_repository: CheckAccountByEmailRepository,
    ) -> None:
        self.__hasher = hasher
        self.__add_account_repository = add_account_repository
        self.__check_account_by_email_repository = check_account_by_email_repository

    def add(self, account: AddAccountParams) -> bool:
        is_valid = False
        exists = self.__check_account_by_email_repository.check_by_email(account.email)
        if not exists:
            hashed_password = self.__hasher.hash(account.password)
            is_valid = self.__add_account_repository.add(
                {**account, "password": hashed_password}
            )
        return is_valid
