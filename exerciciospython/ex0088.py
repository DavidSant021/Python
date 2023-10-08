from random import randint
from time import sleep
lista = list()
jogos = list()
print('_' * 30)
print('      JOGA NA MEGA SENA    ')
print('_' * 30)
quant = int(input('Quantos Jogos Deseja Sortear? '))
tot = 1
while tot <= quant:
    contnum = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contnum += 1
        if contnum >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'=-=' * 11)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('Boa sorte!!!')
