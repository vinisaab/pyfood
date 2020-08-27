# Contexto
from flask.globals import request
import views
from flask import Flask
from flask.admin import Admin
app = Flask(__name__)

## 1 Configuração
### Adicionar Configuração
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DB_URI"] = "mysql://...."

### Registrar rotas
@app.route("/")
def index():
    return "aaaaa"

app.add_url_rule("/inicio", index())

### Iniciar extensões
Admin.init_app(app)

### Registrar blueprints
app.register_blueprint(...)

### Adicionar hooks
app.before_request(...)
app.before_request_funcs(...)

### chamar factories
views.init_app(app)

## App
### App está pronto. Iniciado porém sem request

### Testes
app.teste_client()
#debug
#importar objetos globais (request, session, g)

### Outros hooks

## Request
### Após o primeiro request
from flask import Request
request.args
request.form


