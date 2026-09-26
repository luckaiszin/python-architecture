from ex_24 import media
from ex_25 import criar_perfil_optimal

def aplicar(func, *args, **kwargs):

    print(func(*args,**kwargs))


if __name__ == "__main__":

    notas = [8.1, 5.6, 7.2, 6.3]
    aplicar(media,*notas)
    aplicar(criar_perfil_optimal,"Ana", idade=25, cidade="SP")
