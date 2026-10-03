from typing import Callable

# Sem TypeAlias: a assinatura fica gigante e difícil de ler
def processar_dados(callback: Callable[[int, str, list[float]], bool | None]) -> None:
    pass

# Com TypeAlias (Python 3.12+):
type HandlerCallback = Callable[[int, str, list[float]], bool | None]

def processar_dados(callback: HandlerCallback) -> None:
    pass