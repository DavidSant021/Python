lista1 = []
lista2 = []
maiorp = menorp = 0
while True:
    lista2.append(str(input('Nome: ')))
    lista2.append(float(input('Peso: ')))
    if len(lista1) == 0:
        maiorp = menorp = lista2[1]
    else:
        if lista2[1] > maiorp:
            maiorp = lista2[1]
        if lista2[1] < menorp:
            menorp = lista2[1]
    lista1.append(lista2[:])
    lista2.clear()
    op = ' '
    while op not in 'SsNn':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op in 'N':
        break
print('=-=' * 25)
print(f'Ao todo você cadastrou {len(lista1)} pessoas.')
print(f'O maior peso foi {maiorp}Kg. Peso de ', end='')
for p in lista1:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menorp}Kg. Peso de ', end='')
for p in lista1:
    if p[1] == menorp:
        print(f'[{p[0]}]', end='')
print()
print('Fim')
