def busca(lista: list, valor: int) -> int:

    for indice, elemento in enumerate(lista):
        if elemento == valor:
            return indice
        
    return -1

lista = [10,12,14,72,56,65,34,28]
v = 72

print(f"o valor {v} esta no indice {busca(lista,v)}")