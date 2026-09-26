def criar_multiplicador(fator):
    # 'fator' pertence ao escopo da função externa
    def multiplicar(numero):
        # A função interna usa a variável 'fator' do escopo pai
        return numero * fator

    return multiplicar # Retorna a função em si, sem executar

if __name__ == "__main__":

    dobrar = criar_multiplicador(2)
    triplicar = criar_multiplicador(3)
    print(dobrar(5))
    print(triplicar(3))