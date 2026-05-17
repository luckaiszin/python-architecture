import json

json_str = '{"alunos": [{"nome": "Ana", "nota": 8.5}, {"nome": "Pedro", "nota": 6.0}]}'

json_dict = json.loads(json_str)

with open('alunos.json','w') as file:
    json.dump(json_dict,file, indent=4)

alunos = json_dict['alunos']

soma_notas = sum(aluno['nota'] for aluno in alunos)
media = soma_notas/len(alunos)

json_dict['media'] = media

with open('turma.json','w') as f:
    json.dump(json_dict,f,indent=4)