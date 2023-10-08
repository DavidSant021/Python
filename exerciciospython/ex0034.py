s = float(input('Digite o seu salário: R$'))
if s <= 1250.00:
    novo = s + (s * 15 / 100)
else:
    novo = s + (s * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(s, novo))
