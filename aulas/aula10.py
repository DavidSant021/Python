n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média é de {}'.format(m))
if m >= 6.0:
    print('Parabéns, sua média foi boa.')
else:
    print('Sua média foi ruim, estude mais.')
