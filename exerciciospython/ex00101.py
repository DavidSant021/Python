def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return print(f'Com {idade} anos: NÃO VOTA.')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')


#  PROGRAMA PRINCIPAL
nasc = int(input('Digite seu ano de nascimento: '))
print(f'{voto(nasc)}')
