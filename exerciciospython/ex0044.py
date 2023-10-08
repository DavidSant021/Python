print('{:=^40}'.format(' Lojas 157 '))
valor = float(input('Digite o valor do produto: R$'))
print('''Opções de pagamento:
[1] À vista Dinheiro/Cheque
[2] À vista no cartão
[3] Até 2x no cartão
[4] 3x ou mais no cartão''')
op = int(input('Digite sua opção de pagamento: '))
if op == 1:
    total = valor - (valor * 10 / 100)
elif op == 2:
    total = valor - (valor * 5 / 100)
elif op == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f}'.format(parcela))
elif op == 4:
    total = valor + (valor * 20 / 100)
    ttlparc = int(input('Deseja parcelar em quantas parcelas? '))
    parcela = total / ttlparc
    print('Sua compra será parcelada em {}x de {:.2f}'.format(ttlparc, parcela))
else:
    total = valor
    print('\033[41mOpção invalida\033[m')
print('Sua compra de {:.2f} vai custar {:.2f} no final.'.format(valor, total))
