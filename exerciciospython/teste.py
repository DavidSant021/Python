cadas = dict()
cadas['Nome'] = str(input('Nome: '))
cadas['Média'] = float(input(f'Média de {cadas["Nome"]}: '))
if cadas['Média'] >= 7:
    cadas['Situação'] = 'Aprovado'
elif cadas['Média'] >= 5 < 7:
    cadas['Situação'] = 'Recuperação'
else:
    cadas['Situação'] = 'Reprovado'
for k, v in cadas.items():
    print(f'{k} é igual a {v}.')
