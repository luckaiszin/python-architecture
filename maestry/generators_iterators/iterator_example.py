class Contador:

    """
    Um Iterator (iterador) é um objeto que representa um fluxo de dados e sabe como retornar um item por vez.
    """
    def __init__(self, limite):
        self.limite = limite
        self.atual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual < self.limite:
            numero = self.atual
            self.atual += 1
            return numero
        else:
            raise StopIteration


if __name__ == "__main__":
# Usando o Iterator
    meu_contador = Contador(3)

    print(next(meu_contador))  # 0
    print(next(meu_contador))  # 1
    print(next(meu_contador))  # 2
    # print(next(meu_contador)) # Lançaria a exceção StopIteration