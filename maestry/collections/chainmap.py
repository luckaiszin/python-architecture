from collections import ChainMap

brinquedos = {"Lego": 30, "Boneco": 10}
informatica = {"Tablet": 5, "Mouse": 15, "Celular":30}
roupas = {"jeans": 150, "Camisa": 100}

estoque = ChainMap(brinquedos, informatica, roupas)

print(estoque) #ChainMap({'Lego': 30, 'Boneco': 10}, {'Tablet': 5, 'Mouse': 15, 'Celular': 30}, {'jeans': 150, 'Camisa': 100})
print(list(estoque.keys()))
print(estoque["Tablet"])