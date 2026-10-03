from typing import Optional

def buscar_usuario(id_usuario: int) -> str | None:
    if id_usuario == 1:
        return "Alice"
    return None

def buscar_usuario_updated(id_usuario: int) -> Optional[str]:
    if id_usuario == 1:
        return "Alice"
    return None

if __name__ == "__main__":
    print(buscar_usuario_updated(2))