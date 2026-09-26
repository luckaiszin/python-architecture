import time

def cronometro(func):

    t_inicio = time.time()
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        t_fim = time.time()
        print(f"Tempo de Execução: {t_fim - t_inicio}")

    return wrapper

@cronometro
def imprimir_sequencia(fator):
    for i in range(fator):
        print(f"sequencia - {i}")


if __name__ == "__main__":

    imprimir_sequencia(555522)
