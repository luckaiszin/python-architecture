from enum import Enum

"""
O Enum serve para criarmos constantes em função de um determinado contexto.
Imagine o seguinte trecho:
    if status == 1:
        enviar_email()
    elif status == 2:
        estornar_dinheiro()

Como eu saberei qual número é para qual situação?
"""

# Classe de Contexto:

class StatusPedido(Enum):

    AGUARDANDO_PAGAMENTO = 1
    PAGO = 2
    CANCELADO = 3

status = StatusPedido.CANCELADO

if status == StatusPedido.AGUARDANDO_PAGAMENTO:
    print("estamos aguardando o pagamento!")
elif status == StatusPedido.PAGO:
    print("pedido despachado!")
else:
    print("pedimos desculpas pelo atraso!")

# Muuito mais elegante!
