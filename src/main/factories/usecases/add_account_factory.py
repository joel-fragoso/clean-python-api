from src.data.usecases import DbAddAccount
from src.domain.usecases import AddAccount
from src.infra.cryptography import BcryptAdapter
from src.infra.db.in_memory import AccountInMemoryRepository


def make_db_add_account() -> AddAccount:
    salt = 12
    bcrypt_adapter = BcryptAdapter(salt)
    account_in_memory_repository = AccountInMemoryRepository()
    return DbAddAccount(
        bcrypt_adapter, account_in_memory_repository, account_in_memory_repository
    )
