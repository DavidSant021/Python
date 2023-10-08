'''pessoas = {'nome': 'David', 'sexo': 'M', 'idade': 21}
pessoas['peso'] = 65.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'Rj'}
estado2 = {'uf': 'São Paulo', 'sigla': 'Sp'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
