from dataclasses import dataclass
import typing as t

from src.data.protocols.db.account import (
    AddAccountRepository,
    AddAccountRepositoryParams,
    CheckAccountByEmailRepository,
    LoadAccountByEmailRepository,
    LoadAccountByEmailRepositoryResult,
    LoadAccountByTokenRepository,
    LoadAccountByTokenRepositoryResult,
    UpdateAccessTokenRepository,
)


@dataclass
class Account:
    id: str
    name: str
    email: str
    password: str

    def to_dict(self) -> t.Dict[str, t.Any]:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
        }

    @staticmethod
    def from_dict(data: t.Dict[str, t.Any]):
        return Account(data["id"], data["name"], data["email"], data["password"])


class AccountInMemoryRepository(
    AddAccountRepository,
    LoadAccountByEmailRepository,
    UpdateAccessTokenRepository,
    LoadAccountByTokenRepository,
    CheckAccountByEmailRepository,
):
    __accounts: list[Account] = []

    def add(self, data: AddAccountRepositoryParams) -> bool:
        self.__accounts.append(Account.from_dict(data.to_dict()))
        return True

    def load_by_email(self, email: str) -> LoadAccountByEmailRepositoryResult | None:
        for account in self.__accounts:
            if email == account.email:
                return LoadAccountByEmailRepositoryResult(
                    account.id, account.name, account.password
                )
        return None

    def check_by_email(self, email: str) -> bool:
        for account in self.__accounts:
            if email == account.email:
                return True
        return False

    def update_access_token(self, id: str, token: str) -> None:
        return None

    def load_by_token(
        self, token: str, role: str | None
    ) -> LoadAccountByTokenRepositoryResult | None:
        return LoadAccountByTokenRepositoryResult("1")
