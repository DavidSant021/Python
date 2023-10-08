somidade = 0
med = 0
maioridh = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('----  {}ª PESSOA  ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somidade += idade
    if p == 1 and sexo in 'Mm':
        maioridh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridh:
        maioridh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
med = somidade / 4
print('A média de idade do gruo é de {} anos'.format(med))
print('O homem mais velho é o {} de {} anos'.format(nomevelho, maioridh))
print('Ao todo tem um total de {} mulher(es) com menos de 20 anos'.format(totmulher20))
