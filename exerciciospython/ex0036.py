vc = float(input('Qual o valor da casa: R$'))
vs = float(input('Quanto você recebe mensalmente? R$'))
a = int(input('Quantos anos de financiamento? '))
# SÓ É APROVADO SE O VALOR DAS PRESTAÇÕES FOREM MENOR OU IGUAL QUE 30% DO SALÁRIO
# SE FOREM MAIOR QUE 30% DO SALÁRIO SERÁ NEGADO
pm = vc / (a * 12)
print('Para pagar uma casa no valor de R${:.2f} em {} anos. '.format(vc, a), end='')
print('As prestações serão de {:.2f}'.format(pm))
if pm > vs * 30 / 100:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo APROVADO')
