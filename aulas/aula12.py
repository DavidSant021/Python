n = str(input('Qual é o seu nome? ')).upper()
if n == 'DAVID':
    print('Seu nome é muito bonito.')
elif n == 'OCLAND' or n == 'ORLANDO':
    print('Seu nome é um pouco diferente.')
elif n in 'MANU ESTER LENILDA':
    print('Seu nome é do gênero feminino.')
else:
    print('Seu nome é meio estranho.')
print('Tenha um bom dia, {}!'.format(n))
