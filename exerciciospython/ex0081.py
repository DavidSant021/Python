lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SsNn':
        op = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if op in 'N':
        break
print('=-=' * 20)
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista de forma decrescente é {lista}')
if 5 in lista:
    print('O valor 5 está na lista.')
else:
    print('O valor 5 não está na lista')
