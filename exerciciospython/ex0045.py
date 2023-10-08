from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[42mSuas opções:\033[m
\033[1;30m[0] PEDRA\033[m
\033[1;35m[1] PAPEL\033[m
\033[1;36m[2] TESOURA\033[m''')
jogador = int(input('\033[42mQual é a sua jogada:\033[m '))
if jogador >= 3:
    print('\033[41mOpção invalida, tente novamente.\033[m')
else:
    print('\033[4;36mJO\033[m')
    sleep(1)
    print('\033[4;32mKEM\033[m')
    sleep(1)
    print('\033[4;33mPO!!!\033[m')
    print(' ')
    print('\033[1;33m-=\033[m' * 15)
    print('\033[1;34mO jogador jogou {}\033[m'.format(itens[jogador]))
    print('\033[1;34mO computador jogou {}\033[m'.format(itens[computador]))
    print('\033[1;33m-=\033[m' * 15)
    if computador == 0:  # computador jogou pedra
        if jogador == 0:
            print('\033[1;33mEMPATE!\033[m')
        elif jogador == 1:
            print('\033[1;32mJOGADOR GANHOU!\033[m')
        elif jogador == 2:
            print('\033[1;31mCOMPUTADOR GANHOU!\033[m')
    elif computador == 1:  # computador jogou papel
        if jogador == 0:
            print('\033[1;31mCOMPUTADOR GANHOU!\033[m')
        elif jogador == 1:
            print('\033[1;33mEMPATE!\033[m')
        elif jogador == 2:
            print('\033[1;32mJOGADOR GANHOU!\033[m')
    elif computador == 2:  # computador jogou tesoura
        if jogador == 0:
            print('\033[1;32mJOGADOR GANHOU!\033[m')
        elif jogador == 1:
            print('\033[1;31mCOMPUTADOR GANHOU!\033[m')
        elif jogador == 2:
            print('\033[1;33mEMPATE!\033[m')
    print('\033[1;33m-=\033[m' * 15)
