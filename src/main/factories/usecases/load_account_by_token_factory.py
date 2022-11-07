from src.data.usecases import DbLoadAccountByToken
from src.domain.usecases import LoadAccountByToken
from src.infra.cryptography import JwtAdapter
from src.infra.db.in_memory import AccountInMemoryRepository


def make_db_load_account_by_token() -> LoadAccountByToken:
    jwt_adapter = JwtAdapter("0123456789")
    account_in_memory_repository = AccountInMemoryRepository()
    return DbLoadAccountByToken(jwt_adapter, account_in_memory_repository)
