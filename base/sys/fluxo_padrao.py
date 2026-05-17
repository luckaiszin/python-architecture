"""
No sistema operacional (como Windows, Linux ou macOS), todo programa
que roda no terminal ganha automaticamente três canais 
de comunicação padrão: um para entrar dados, um para sair dados e um exclusivo para erros. 
O módulo sys do Python nos dá acesso direto a esses três canais.
"""

import sys

# Uma mensagem normal vai para a saída padrão
sys.stdout.write("Processando os dados com sucesso...\n")

# Um aviso de erro vai para o canal de erro padrão
sys.stderr.write("ERRO CRÍTICO: A conexão com o banco de dados falhou!\n")