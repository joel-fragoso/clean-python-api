from flask import current_app as Flask

from src.main.routes import account


def setup_routes(app: Flask) -> None:  # type: ignore
    app.register_blueprint(account)
