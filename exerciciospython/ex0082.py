a = []
while True:
    a.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SsNn':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op in 'Nn':
        break
b = []
c = []
for n in a:
    if n % 2 == 0:
        b.append(n)
    else:
        c.append(n)
print('=-=' * 20)
print(f'A lista é: {a}')
print(f'Os pares da lista são: {b}')
print(f'Os ímpares da lista são: {c}')
