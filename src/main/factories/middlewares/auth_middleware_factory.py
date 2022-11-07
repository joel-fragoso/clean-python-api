from typing import Optional

from src.main.factories.usecases import make_db_load_account_by_token
from src.presentation.middlewares import AuthMiddleware
from src.presentation.protocols import Middleware


def make_auth_middleware(role: Optional[str]) -> Middleware:
    return AuthMiddleware(make_db_load_account_by_token(), role)
