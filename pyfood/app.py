from flask import Flask
from pyfood.ext import site


def create_app():
    """Main Factory

    Returns:
        app: return flask app
    """
    app = Flask(__name__)
    site.init_app(app)
    return app
