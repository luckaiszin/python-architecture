def requer_login(usuario):
    def acessar_login(func):
        def wrapper(*args, **kwargs):
            if usuario != "admin":
                print("ACESSO NEGADO")
                return None

            print("USUÁRIO ACEITO")
            print("Executando a função...")

            resultado = func(*args, **kwargs)
            print("Função executada com sucesso")
            return resultado

        return wrapper

    return acessar_login

@requer_login(usuario="admin")
def painel_admin():
    print("-> Bem-vindo ao painel confidencial!")


@requer_login(usuario="visitante")
def painel_restrito():
    print("-> Tentando acessar...")

if __name__ == "__main__":
    print("--- Teste 1 (Admin) ---")
    painel_admin()

    print("\n--- Teste 2 (Visitante) ---")
    painel_restrito()