from src.main.factories.usecases import make_db_authentication
from src.presentation.controllers import SignInController
from src.presentation.protocols import Controller

from .signin_validation_factory import make_signin_validation


def make_signin_controller() -> Controller:
    return SignInController(make_db_authentication(), make_signin_validation())
