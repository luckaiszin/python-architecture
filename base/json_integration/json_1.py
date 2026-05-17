import json

produto_1 = {
    'nome':'revista',
    'preco' : 10,
    'estoque': 5
}

produto_2 = {
    'nome':'manga',
    'preco' : 15,
    'estoque': 2
}

produto_3 = {
    'nome':'jornal',
    'preco' : 2,
    'estoque': 8
}

with open('produto.json','w') as f:
    json.dump(produto_1,f,indent = 4)

with open('produto.json','r') as f:
    produto_arquivo = json.load(f)

print("Preco: ",produto_arquivo['preco'])