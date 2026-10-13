import asyncio
import time  # Usar o time padrão para medir a performance


async def process_b():
  print("Processo B: Iniciando processamento...")
  await asyncio.sleep(12)  # Simula uma operação assíncrona (ex: requisição HTTP)
  print("Processo B: Concluído!")
  return "Resultado do Processo B"


async def continuar_outro_trabalho():
  print("Processo A: 'Continuando o trabalho' em paralelo...")
  await asyncio.sleep(5)  # Faz outra coisa útil enquanto o B processa
  print("Processo A: Trabalho paralelo concluído.")


async def process_a():
  print("Processo A: Iniciando...")
  print("Processo A: Enviando solicitação para o Processo B...")

  # Dispara o Processo B como uma tarefa, sem bloquear o fluxo imediato
  tarefa_b = asyncio.create_task(process_b())

  # O Processo A continua executando outras tarefas (Continue working)
  await continuar_outro_trabalho()

  # O Processo A agora busca a resposta do Processo B (Get Response)
  resposta_b = await tarefa_b

  print(f"Processo A: Resposta recebida: '{resposta_b}'")
  print("Processo A: Finalizado!")


# Executando o fluxo assíncrono com time.perf_counter()
if __name__ == "__main__":
  inicio = time.perf_counter()  # Medição de tempo robusta e segura

  asyncio.run(process_a())

  fim = time.perf_counter()
  print(f"Tempo total assíncrono: {fim - inicio:.2f}s")