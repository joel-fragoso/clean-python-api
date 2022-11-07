from flask import Blueprint

from src.main.adapters import adapt_route
from src.main.factories.controllers import make_signin_controller

account = Blueprint("account", __name__)

account.post("/signin")(adapt_route(make_signin_controller()))
