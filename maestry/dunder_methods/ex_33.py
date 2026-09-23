class Produto:

    def __init__(self, nome:str, preco:float):
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:

        return f"Produto: {self.nome} - R$ {self.preco}"

    def __repr__(self) -> str:

        return f"Produto({self.nome}, {self.preco})"

p1 = Produto("Camiseta", 24.88)

print(p1)
print(repr(p1))