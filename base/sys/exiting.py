import sys

usuario_autorizado = False

if not usuario_autorizado:
    print("Acesso negado. Fechando o programa...")
    sys.exit()  # O script para aqui

print("Isso nunca será impresso.")