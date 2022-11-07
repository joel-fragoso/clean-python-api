from flask import Flask


def create_app(config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        from src.main.config import setup_routes

        setup_routes(app)

    return app
