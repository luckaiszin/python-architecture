import csv

# 1. Criação/Escrita do arquivo
dados = [
    ['nome', 'nota1', 'nota2'],
    ['pata', 6, 8],      # Média: 7.0
    ['peta', 7, 6.4],    # Média: 6.7
    ['pita', 7, 8.5],    # Média: 7.75  ✓
    ['pota', 7, 9.6],    # Média: 8.3   ✓
    ['monica', 7, 4]       # Média: 5.5
]

with open('alunos.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(dados)


# 2. Leitura e cálculo da média
with open('alunos.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    # Pula a primeira linha (cabeçalho)
    next(reader) 
    
    print("Alunos com média maior que 7:")
    for linha in reader:
        nome = linha[0]
        nota1 = float(linha[1]) # Converte o texto para número decimal
        nota2 = float(linha[2])
        
        media = (nota1 + nota2) / 2
        
        if media > 7:
            print(f"- {nome}: média {media:.2f}")