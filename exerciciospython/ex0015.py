#Saber quanto de gasto dará alugar um carro e pagar por dia e km rodado#
d = int(input('Quantos dias alugados?'))
km = float(input('Qual a distância percorrida? km'))
vp = (d * 60) + (km * 0.15)
print('Somando o valor de {} dias com o valor de {} Km, dará um total de: R${:.2f}'.format(d, km, vp))
