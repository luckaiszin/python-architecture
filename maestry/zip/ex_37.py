
produtos = ["Mouse", "Teclado", "Monitor"] 
precos = [79.9, 149.9, 899.9]
estoques = [150, 80, 25]

compendium = []
for produto, preco, estoque in zip(produtos, precos, estoques):

    elemento = {
        "produto": produto,
        "preco": preco,
        "estoque": estoque
    }

    compendium.append(elemento)

print(compendium)
