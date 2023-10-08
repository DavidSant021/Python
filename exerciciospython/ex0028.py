from random import randint
from time import sleep  # Esperar tempo para mostrar o print
print("-=-" * 25)
print('Vou pensar em um número de 0 a 5. Tente adivinhar... ')
print('-=-' * 25)
n = int(input('Em que número eu pensei? '))  # eu tento acertar
print('Processando...')
sleep(3)
comp = randint(0, 5)  # computador sorteia um número entre  os escolhidos
if n == comp:
    print('Eu pensei no número {}, PARABÉNS VOCÊ ACERTOU!'.format(comp))
else:
    print('O número que eu pensei foi {}. VOCÊ ERROU *_*'.format(comp))
