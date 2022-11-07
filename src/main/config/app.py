from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        from src.main.config import setup_routes

        setup_routes(app)
        return app
