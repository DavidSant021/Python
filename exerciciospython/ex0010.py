#Converter valores de moedas#
v = float(input('Quanto você tem na carteira? R$:'))
d = v / 4.97
e = v / 5.40
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(v, d, e))
