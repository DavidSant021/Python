from random import randint
v = 0
print('=-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 20)
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    print('=-=' * 20)
    print(f'Você jogou {jogador} e o computador {computador} o total é {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu.')
            v += 1
            print('=-=' * 20)
        else:
            print('Você perdeu.')
            print('=-=' * 20)
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu.')
            v += 1
            print('=-=' * 20)
        else:
            print('Você perdeu.')
            print('=-=' * 20)
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. Você Ganhou {v} vezes')
