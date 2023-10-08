v = float(input('Qua é a velocidade atual do carro? '))
m = (v - 80) * 7.00
if v > 80:
    print('MULTADO! Você exedeu o limite que é de 80Kmh\n Você deve pagar uma multa de R${:.2f}'.format(m))
print('Tenha um bom dia! Dirija com segurança.')
