from collections import defaultdict

dic_bonus = defaultdict(list)

vendas = {"Andre": 1000, "Joao": 2000, "Lira": 500, "Amanda": 1500, "Carol": 3000, "Marcos":200, "Camila":2000}
meta1 = 1000
meta2 = 2000

for vendedor, vendas in vendas.items():
    if vendas > meta2:
        dic_bonus["meta2"].append(vendedor)
    elif vendas > meta1: 
        dic_bonus["meta1"].append(vendedor)
    else:
        dic_bonus["sem meta"].append(vendedor)

print(dic_bonus)