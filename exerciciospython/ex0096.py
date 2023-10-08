def lin():
    print('_' * 24)
    print('  Controle De Terrenos  ')
    print('_' * 24)


def area(a, b):
    mq = a * b
    print(f'A área de um terreno {a}x{b} é de {mq}m².')


#  Porgrama Principal
lin()
larg = float(input('LARGURA (m): '))
comp = float(input('COMPRIMENTO (m): '))
area(larg, comp)
