#Cálculo de desconto com porcentagem#
v = float(input('Digite o valor do produto? R$:'))
pd = v*5/100
nv = v-pd
print('O produto tem o valor de R${} e na promoção com 5% de desconto sairá por: R${:.2f}.\n Total descontado será de: R${:.2f}'.format(v, nv, pd))
