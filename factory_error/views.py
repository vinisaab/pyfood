"""Extensão de views do flask
"""
def init_app(app):
    @app.route("/")
    def index():
        return "Hello Word"

    @app.route("/contato")
    def contato():
        return "<form>NOME: <input type='text'></input><form>"


