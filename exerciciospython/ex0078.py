numeros = []
maior = 0
menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print('=-=' * 15)
print(f'O maior valor foi {maior} nas posições', end='')
for p, v in enumerate(numeros):
    if maior == v:
        print(f' {p}...', end=' ')
print(f'\nO menor valor foi {menor} nas posições', end='')
for p, v in enumerate(numeros):
    if menor == v:
        print(f' {p}...', end=' ')
print()
print('=-=' * 15)
