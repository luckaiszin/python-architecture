def criar_perfil(nome, **kwargs):

    perfil = {}

    if nome:
        perfil["nome"] = nome
        for k,v in kwargs.items():
            perfil[k] = v

    return perfil

def criar_perfil_optimal(nome, **kwargs):

    perfil = {"nome" : nome, **kwargs}
    return perfil


if __name__ == "__main__":

    print(criar_perfil_optimal("Ana", idade=25, cidade="SP"))