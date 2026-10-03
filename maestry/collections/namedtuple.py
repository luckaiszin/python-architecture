from collections import namedtuple

Produto = namedtuple("Produto", ["nome","preco","tamanho"])

p1 = Produto("Jeans",10,"M")

print(p1.nome)
print(p1[0])

