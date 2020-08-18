import views
from flask import Flask


def create_app():
    """Factory Principal

    Returns:
        app: App principal
    """
    app = Flask(__name__)
    views.init_app(app)
    return app
