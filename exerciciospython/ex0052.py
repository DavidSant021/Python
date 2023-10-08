n = int(input('Digite um número: '))  # Ler o número
cont = 0
for c in range(1, n + 1):  # Verificando todos que divididos pelo c o resto é zero
    if n % c == 0:
        print('\033[32m', end='')  # Mostro todos divisíveis com resto 0 em verde
        cont += 1  # Conto quantos foram divisiveis
    else:
        print('\033[31m', end='')  # Mostro todos q não foram divisiveis em vermelho
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, cont))
if cont == 2:  # Se tem 2 divisiveis é primo
    print('Por isso É PRIMO')
else:  # Se tem mais de 2 divisiveis não é primo
    print('Por isso NÃO É PRIMO')
