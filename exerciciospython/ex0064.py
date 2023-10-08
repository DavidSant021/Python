cont = s = 0
print('Digite 999 para finalizar')
n = int(input('Digite um número: '))
while n != 999:
    cont += 1
    s += n
    n = int(input('Digite um número: '))
print('Você digitou {} números e a soma de todos é de {}'.format(cont, s))
