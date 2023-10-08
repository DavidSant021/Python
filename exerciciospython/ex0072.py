cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
        'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
        'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
        'Dezenove', 'Vinte')
while True:
    print('=-=' * 20)
    print('Digite um número entre 0 e 20:')
    print('=-=' * 20)
    num = int(input('Digite um número para ver por extenso: '))
    while not 0 <= num <= 20:
        num = int(input('Tente novamente. Digite um número para ver por extenso: '))
    print(f'Você escreveu {cont[num]}')
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? ')).strip().upper()[0]
    if op in 'N':
        break
