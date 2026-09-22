from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "mensagem": "API funcionando com sucesso!"
    }


def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json()["status"] == "online"


def test_listar_usuarios():
    response = client.get("/usuarios")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_buscar_usuario_existente():
    response = client.get("/usuarios/1")
    assert response.status_code == 200
    assert response.json()["nome"] == "Ana"


def test_buscar_usuario_inexistente():
    response = client.get("/usuarios/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Usuário não encontrado"