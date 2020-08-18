# Contexto
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
app.register_blueprint(....)

### Adicionar hooks
app.before_request(...)
app.after_request(...)

### chamar factories
## App


## Request