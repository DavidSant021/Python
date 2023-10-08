from datetime import date
ano = int(input('Digite um ano para saber se é BISSEXTO ou 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} É BISSEXTO.'.format(ano))
else:
    print('O ano de {} NÃO É BISSEXTO'.format(ano))
