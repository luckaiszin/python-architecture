# Exemplo extraído da Hashtag Programação

import time
import asyncio


async def calcular_imposto(faturamento):
    print(faturamento*0.1)

async def calcular_bonus_funcionarios(vendas):
    for funcionario,venda in vendas.items():
        print(funcionario, "Bonus: ", venda*0.05)
        await asyncio.sleep(2)

async def fechamento():

    vendas = {
        "Ted": 1500,
        "Laika": 500,
        "Garoto": 5000
    }

    faturamento = 1000
    tarefa_1 = asyncio.create_task(calcular_bonus_funcionarios(vendas))
    tarefa_2 = asyncio.create_task(calcular_imposto(faturamento))
    await tarefa_1
    await tarefa_2
    print("[FINALIZADO]")

asyncio.run(fechamento())