def metade(n=0, form=False):
    res = n / 2
    return res if form is False else moeda(res)


def dobro(n=0, form=False):
    res = n * 2
    return res if form is False else moeda(res)


def aumentar(n=0, p=0, form=False):
    res = n + (n * p / 100)
    return res if form is False else moeda(res)


def diminuir(n=0, p=0, form=False):
    res = n - (n * p / 100)
    return res if form is False else moeda(res)


def moeda(n=0, moedas='R$'):
    return f'{moedas}{n:>.2f}'.replace('.', ',')


def resumo(n=0, s=10, su=5):
    print('_' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('_' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{s}% de aumento: \t{aumentar(n, s, True)}')
    print(f'{su}% de redução: \t{diminuir(n, su, True)}')
    print('_' * 30)
