
def test_app_is_created(app):
    assert app.name == "pyfood.app"


def test_config_is_load(config):
    assert config["DEBUG"] is False


def test_request_returns_404(client):
    assert client.get("/url_que_nao_existe").status_code == 404
