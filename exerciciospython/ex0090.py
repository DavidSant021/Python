cadastro = dict()
cadastro['Nome'] = str(input('Nome: '))
cadastro['Média'] = float(input(f'Média de {cadastro["Nome"]}: '))
if cadastro['Média'] >= 7:
    cadastro['Situação'] = 'Aprovado'
elif 5 <= cadastro['Média'] < 7:
    cadastro['Situação'] = 'Recuperação'
else:
    cadastro['Situação'] = 'Reprovado'
print('-=' * 35)
for k, v in cadastro.items():
    print(f'  - {k} é igual a {v}')
