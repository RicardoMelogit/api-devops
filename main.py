from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="API Docker",
    description="API simples desenvolvida para a disciplina de DevOps",
    version="1.0.0"
)


class Usuario(BaseModel):
    nome: str
    email: str


usuarios = [
    {"id": 1, "nome": "Ana", "email": "ana@email.com"},
    {"id": 2, "nome": "Carlos", "email": "carlos@email.com"}
]


@app.get("/")
def home():
    return {
        "mensagem": "API funcionando com sucesso!"
    }


@app.get("/status")
def status():
    return {
        "status": "online",
        "aplicacao": "API Python - Atividade DevOps"
    }


@app.get("/usuarios")
def listar_usuarios():
    return usuarios


@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            return usuario

    raise HTTPException(
        status_code=404,
        detail="Usuário não encontrado"
    )


@app.post("/usuarios", status_code=201)
def criar_usuario(usuario: Usuario):
    novo_usuario = {
        "id": len(usuarios) + 1,
        "nome": usuario.nome,
        "email": usuario.email
    }

    usuarios.append(novo_usuario)

    return novo_usuario