from ex00115.lib.interface import *
from ex00115.lib.arquivo import *
from time import sleep
c = ['\033[m',
     '\033[1;31m',
     '\033[1;32m',
     '\033[1;33m',
     '\033[1;34m',
     '\033[1;35m']

arq = ('cursoemvideo.txt')

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #  Opção de listar o conteudo de um arquivo
        lerarquivo(arq)
    elif resposta == 2:
        #  Opção de cadastrar uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome:'))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho(f'{c[1]}Saindo do sistema... Até logo!{c[0]}')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
