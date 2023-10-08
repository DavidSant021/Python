from datetime import date
totma = 0
totme = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = date.today().year - ano
    if idade >= 21:
        totma += 1
    else:
        totme += 1
print('Ao todos temos {} pessoas maiores de idade e {} menores de idade'.format(totma, totme))
