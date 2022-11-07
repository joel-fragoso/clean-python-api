from src.main.factories.usecases import make_db_add_account, make_db_authentication
from src.presentation.controllers import SignUpController
from src.presentation.protocols import Controller

from .signup_validation_factory import make_signup_validation


def make_signup_controller() -> Controller:
    return SignUpController(
        make_db_add_account(), make_signup_validation(), make_db_authentication()
    )
