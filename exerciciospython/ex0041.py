from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {} anos de idade e sua categoria é MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos de idade e sua categoria é INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos de idade e sua categoria é JUNIOR.'.format(idade))
elif idade <= 25:
    print('Você tem {} anos de idade e sua categoria é SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos de idade e sua categoria é MASTER.'.format(idade))
