"""
Um iterator que utiliza o yield
"""

def contador_gerador(limite):
    atual = 0
    while atual < limite:
        yield atual
        atual += 1

# Usando o Generator

if __name__ == "__main__":
    gen = contador_gerador(8)

    print(next(gen))  
    print(next(gen))  
    print(next(gen))  