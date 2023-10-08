# Botar nome em maiúsculo, minúsculo, saber quantas letras sem spawn e quantas letrar no primeiro nome
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...\nSeu nome em maiúsculas é {}.'.format(nome.upper()))
print('Seu nome em minúsculas {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
dvd = nome.split()
print('Seu primeiro nome {}, Tem {} letras no primeiro nome.'.format(dvd[0], len(dvd[0])))
