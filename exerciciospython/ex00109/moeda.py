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
