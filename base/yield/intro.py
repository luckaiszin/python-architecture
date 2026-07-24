def contador_com_return():
    return [1, 2, 3]

# Retorna a lista inteira de uma vez só
print(contador_com_return())  # Saída: [1, 2, 3]

def contador_com_yield():
    yield 1
    yield 2
    yield 3

# Cria o gerador, mas não executa o código ainda
meu_gerador = contador_com_yield()

# Pegando os valores um por um
print(next(meu_gerador))  # Saída: 1 (a função pausa aqui)
print(next(meu_gerador))  # Saída: 2 (a função continua e pausa aqui)
print(next(meu_gerador))  # Saída: 3 (a função continua e pausa aqui)