#Sorteio de 1#
from random import choice
n1 = str(input('Digite o primeiro nome:'))
n2 = str(input('Digite o segundo nome:'))
n3 = str(input('Digite o terceiro nome:'))
n4 = str(input('Digite o quarto nome:'))
lista = [n1, n2, n3, n4]
print('_' * 20)
print('O nome escolhido foi: {}'.format(choice(lista)))
print('_' * 20)
