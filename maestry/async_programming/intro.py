# Exemplo extraído da Hashtag Programação

import time


def calcular_imposto(faturamento):
    print(faturamento*0.1)

def calcular_bonus_funcionarios(vendas):
    for funcionario,venda in vendas.items():
        print(funcionario, "Bonus: ", venda*0.05)
        time.sleep(2)

def fechamento():

    vendas = {
        "Ted": 1500,
        "Laika": 500,
        "Garoto": 5000
    }

    faturamento = 1000
    calcular_bonus_funcionarios(vendas)
    calcular_imposto(faturamento)
    print("[FINALIZADO]")

fechamento()