from flask import Flask

from src.main.routes import account


def setup_routes(app: Flask) -> None:
    app.register_blueprint(account)
