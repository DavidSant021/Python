op = 'S'
med = cont = soma = menor = maior = 0
while op in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
med = soma / cont
print('A média dos {} valores lidos é de {}'.format(cont, med))
print('O maior valor lido é {} e o menor lido é {}'.format(maior, menor))
