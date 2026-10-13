import time

def processo_b():
    print("Processo B: Iniciando processamento...")
    time.sleep(5)
    print("Processo B: Concluído!")
    return "Processo B Completo"

def processo_a():
    print("Processo A: Iniciando processamento...")
    print("Enviando requisição ao processo B...")
    time.sleep(1)

    resposta_b = processo_b()

    print(f"Processo A: Resposta recebida: '{resposta_b}'")
    print("Processo A: Continuando o restante do trabalho...")
    time.sleep(2)
    print("Processo A: Finalizado!")


if __name__ == "__main__":

    inicio = time.time()
    processo_a()
    print(f"Tempo total síncrono: {time.time() - inicio:.2f}s")
