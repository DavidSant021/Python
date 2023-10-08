from datetime import date
print('''Opções:
[1] \033[1;34mMasculino\033[m
[2] \033[1;31mFeminino\033[m''')
op = int(input('Digite a opção de acordo com seu sexo: '))
if op == 2:
    print('\033[41mVocê não precisa se alistar.\033[m')
elif op == 0 or op > 2:
    print('\033[41mOpção invalida\033[m')
else:
    print('\033[42mVocê precisa se alistar.\033[m')
    ano = int(input('\033[43mMe diga o seu ano de nascimento:\033[m '))
    idade = date.today().year - ano
    atual = date.today().year
    if idade < 18:
        falta = 18 - idade
        print('\033[32mIdade insuficiente para se alistar.\nFaltam apenas {} ano(s).\033[m'.format(falta))
        sera = atual + falta
        print('\033[32mSeu alistamento será no ano de {}.\033[m'.format(sera))
    elif idade == 18:
        print('\033[36mJá é sua hora de se alistar ao serviço militar.\033[m')
    elif idade > 18:
        passou = idade - 18
        print('\033[31mVocê precisa se alistar ao serviço militar.\nPassou um total de {} ano(s).\033[m'.format(passou))
        foi = atual - passou
        print('\033[31mSeu alistamento seria no ano de {}.\033[m'.format(foi))
