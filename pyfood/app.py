from flask import Flask

def create_app():
    """Main Factory

    Returns:
        app: return flask app
    """
    app =  Flask(__name__)
    return app