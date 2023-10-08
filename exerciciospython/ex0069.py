contmi = contm2 = conth = 0
while True:
    print('=-=' * 9)
    print('    CADASTRE UMA PESSOA   ')
    print('=-=' * 9)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        contmi += 1
    if sexo in 'Mm':
        conth += 1
    if sexo in 'Ff' and idade < 20:
        contm2 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if op in 'Nn':
        break
print('=-=' * 9)
print(f'''Total de pessoas com mais de 18 anos de idade é de {contmi}.
Total de {conth} homen(s) cadastrados.
Total de {contm2} mulher(es) com menos de 20 anos cadastradas.''')
