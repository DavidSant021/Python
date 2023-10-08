n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = (n1+n2)
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
print('A soma entre {0}{1}{2} e {3}{4}{5} é igual a {6}{7}{8}.'.format(cores['branco'], n1, cores['limpa'], cores['azul'], n2, cores['limpa'], cores['vermelho'], s, cores['limpa']))
