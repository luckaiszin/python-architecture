from typing import Any

# Variáveis simples
nome: str = "Alice"
idade: int = 30
preco: float = 19.90
ativo: bool = True

#desativa a verificação de tipo para a variável(imprevisivel)
dados: Any = 5

# Função
def saudar(nome: str) -> str:
    return f"Olá, {nome}"

# Função sem retorno
def log_mensagem(msg: str) -> None:
    print(msg)

if __name__ == "__main__":

    saudacao = saudar("Mandioca")
    log_mensagem(saudacao)