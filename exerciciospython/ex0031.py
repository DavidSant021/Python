p = float(input('Quantos Km tem a sua viagem? '))
preco = p * 0.50 if p <= 200 else p * 0.45
print('A sua passagem custará R${:.2f}'.format(preco))
