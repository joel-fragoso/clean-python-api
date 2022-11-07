from typing import Optional

from src.data.protocols.db.account import (
    AddAccountRepositoryParams,
    AddAccountRepository,
    LoadAccountByEmailRepositoryResult,
    LoadAccountByEmailRepository,
    UpdateAccessTokenRepository,
    LoadAccountByTokenRepositoryResult,
    LoadAccountByTokenRepository,
    CheckAccountByEmailRepository,
)


class AccountInMemoryRepository(
    AddAccountRepository,
    LoadAccountByEmailRepository,
    UpdateAccessTokenRepository,
    LoadAccountByTokenRepository,
    CheckAccountByEmailRepository,
):
    __accounts: list[object]

    def add(self, data: AddAccountRepositoryParams) -> bool:
        self.__accounts.append(data)
        return True

    def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult:
        return LoadAccountByEmailRepositoryResult("1", "John Doe", "12345")

    def check_by_email(self, email: str) -> bool:
        return True

    def update_access_token(self, id: str, token: str) -> None:
        return None

    def load_by_token(
        self, token: str, role: Optional[str]
    ) -> Optional[LoadAccountByTokenRepositoryResult]:
        return LoadAccountByTokenRepositoryResult("1")
