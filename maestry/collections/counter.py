from collections import Counter

estoque = ["iphone","iphone","ipad","imac","ipod","ipad"]
contagem_estoque = Counter(estoque)
print(contagem_estoque) #Counter({'iphone': 2, 'ipad': 2, 'imac': 1, 'ipod': 1})
print(contagem_estoque["iphone"])