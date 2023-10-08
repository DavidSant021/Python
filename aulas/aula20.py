def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')


#  Programa Principal
#  n1 = int(input('Primeiro Número: '))
#  n2 = int(input('Segundo Número: '))
#  soma(4, 5)
#  soma(8, 9)
#  soma(2, 1)
#  soma(n1, n2)
#  soma(b=4, a=5)
#  soma(7, 2)

def contador(*num):
    for n in num:
        print(f'{n} ', end='')
    print('Fim!')


#  contador(2, 1, 7)
#  contador(8, 0)
#  contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)
