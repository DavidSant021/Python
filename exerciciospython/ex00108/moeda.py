def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, p=0):
    res = n + (n * p / 100)
    return res


def diminuir(n=0, p=0):
    res = n - (n * p / 100)
    return res


def moeda(n=0, moedas='R$'):
    return f'{moedas}{n:>.2f}'.replace('.', ',')
