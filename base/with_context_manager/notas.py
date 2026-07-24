with open ('notas.txt','w') as notas:
    notas.write('Laika: 10.00\n')
    notas.write('Ted: 7.50\n')
    notas.write('Lucas: 4.00')

with open('notas.txt','r') as notas:
    conteudo = notas.read()
    
print(conteudo)

