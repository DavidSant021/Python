totp = totmm = cont = menorp = 0
maisb = ''
print('<->' * 7)
print('      LOJA 171     ')
print('<->' * 7)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    totp += preco
    cont += 1
    if preco > 1000:
        totmm += 1
    if cont == 1 or preco < menorp:
        menorp = preco
        maisb = nome
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op in 'Nn':
        break
print(f'''Total da compra foi {totp:.2f}
Temos {totmm} custando mais de R$1.000.00
O produto mais barato foi {maisb} que custa R${menorp:.2f}''')
