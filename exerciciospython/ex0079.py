lista = []
while True:
    v = int(input('Digite um valor: '))
    if v not in lista:
        lista.append(v)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não irei adicionar...')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if op in 'Nn':
        break
lista.sort()
print('=-=' * 20)
print(f'Você digitou os valores {lista}')
