#Reajuste salárial#
s = float(input('Qual seu salário? R$'))
sd = s + (s * 15 / 100)
print('Seu salário era de R${:.0f} e com o aumento de 15% seu novo salario será de:R${:.0f}'.format(s, sd))
