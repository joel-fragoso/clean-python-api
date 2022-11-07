from flask import Blueprint

from src.main.adapters import adapt_route
from src.main.factories.controllers import (
    make_signin_controller,
    make_signup_controller,
)

account = Blueprint("account", __name__)

account.post("/signup", endpoint="signup")(adapt_route(make_signup_controller()))
account.post("/signin", endpoint="signin")(adapt_route(make_signin_controller()))
