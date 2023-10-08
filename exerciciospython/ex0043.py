peso = float(input('Digite seu peso: (Kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Grau de {:.1f} ABAIXO DO PESO CUIDADO!'.format(imc))
elif 18.5 <= imc < 25:
    print('Grau de {:.1f} PESO IDEAL!'.format(imc))
elif 25 <= imc < 30:
    print('Grau de {:.1f} SOBREPESO ATENÇÃO!'.format(imc))
elif 30 <= imc < 40:
    print('Grau de {:.1f} OBESIDADE CUIDADO!'.format(imc))
else:
    print('Grau de {:.1f} OBESIDADE MÓBIDA MUITO CUIDADO!'.format(imc))
