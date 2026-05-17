import sys

numeros = sys.argv[1:]

numeros_int = list(map(int,numeros))

print(f"Soma: {sum(numeros_int)}")