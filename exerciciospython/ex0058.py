from random import randint
computador = randint(0, 10)
acertou = False  # acertou ainda não aconteceu, é falso.
tentativas = 0
print('\033[1;34m-=\033[m' * 25)
print(''' \033[1;36mOlá eu sou seu computador.
 Irei pensar em um número entre 0 e 10.
 Tente advinhar!\033[m''')
print('\033[1;34m-=\033[m' * 25)
while not acertou:  # enquanto acertou não é verdadeiro
    jogador = int(input('\033[1;32mQual é o seu palpite?\033[m '))
    tentativas += 1
    if computador == jogador:
        acertou = True  # acertou é verdadeiro se for igual, e sendo verdadeiro finaliza o while
    else:
        if jogador < computador:
            print('\033[1;34m-=\033[m' * 25)
            print('\033[1;31mUm pouco mais.\033[m', end=' ')
        elif jogador > computador:
            print('\033[1;34m-=\033[m' * 25)
            print('\033[1;33mUm pouco menos.\033[m', end=' ')
print('\033[1;34m-=\033[m' * 25)
print('\033[1;32mParabéns você acertou. Foi preciso {} tentativas.\033[m'.format(tentativas))
