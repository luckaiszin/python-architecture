from typing import Callable

# Aceita uma função que recebe dois floats e retorna um float
def aplicar_operacao(a: float, b: float, operacao: Callable[[float, float], float]) -> float:
    return operacao(a, b)