from src.data.usecases import DbAuthentication
from src.domain.usecases import Authentication
from src.infra.cryptography import BcryptAdapter, JwtAdapter
from src.infra.db.in_memory import AccountInMemoryRepository


def make_db_authentication() -> Authentication:
    salt = 12
    bcrypt_adapter = BcryptAdapter(salt)
    jwt_adapter = JwtAdapter("0123456789")
    account_in_memory_repository = AccountInMemoryRepository()
    return DbAuthentication(
        account_in_memory_repository,
        bcrypt_adapter,
        jwt_adapter,
        account_in_memory_repository,
    )
