from datetime import date
cadastro = dict()
print('-=' * 35)
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
cadastro['idade'] = date.today().year - nasc
op = ' '
while op not in 'SsNn':
    print('-=' * 35)
    op = str(input('Tem carteira de Trabalho? ')).strip().upper()[0]
if op in 'Ss':
    cadastro['CTPS'] = int(input('CTPS: '))
    cadastro['anodecont'] = int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Seu salário: R$'))
    cadastro['aposent'] = cadastro['idade'] + ((cadastro['anodecont'] + 35) - date.today().year)
print(f'O seu nome é {cadastro["nome"]}')
print(f'Sua idade é {cadastro["idade"]}')
if op in 'Nn':
    print('Você não possui carteira de trabalho.')
elif op in 'Ss':
    print(f'Sua carteira de trabalho é {cadastro["CTPS"]}')
    print(f'Você foi contratado em {cadastro["anodecont"]}')
    print(f'Seu salário é de {cadastro["salario"]}')
    print(f'Você vai se aposentar com {cadastro["aposent"]} anos')
    salariotot = (cadastro['salario'] * 12) * 35
    print(f'Seu salário do ano de contratação ate se aposentar será um total de {salariotot}')
print('-=' * 35)
print('Fim')
