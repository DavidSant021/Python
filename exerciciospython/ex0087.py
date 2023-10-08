lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
smp = colu = seglinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para a posição {l},{c}: '))
        if lista[l][c] % 2 == 0:
            smp += lista[l][c]
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
print('=-' * 30)
print(f'A soma dos pares é {smp}')
for l in range(0, 3):
    colu += lista[l][2]
print(f'A soma dos valores da terceira coluna é {colu}')
for c in range(0, 3):
    if c == 0 or lista[1][c] > seglinha:
        seglinha = lista[1][c]
print(f'O maior valor da segunda linha é {seglinha}')
