from typing import TypedDict

class Usuario(TypedDict):
    id: int
    nome: str
    admin: bool

u: Usuario = {"id": 1, "nome": "Alice", "admin": True}

print(u)