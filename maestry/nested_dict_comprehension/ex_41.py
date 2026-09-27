resultados = {'Ana': 7.5, 'Pedro': 4.0, 'Maria': 9.0, 'Joao': 5.5}

aprovacoes = {nome: 'aprovado' if nota >= 6 else 'reprovado' for nome, nota in resultados.items()}

print(aprovacoes)