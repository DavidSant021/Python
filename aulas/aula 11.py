# como usar cores
print('\033[31;43mOlá mundo\033[m')
# exemplos
a = 2
b = 3
print('Os valores são \033[1;35m{}\033[m e \033[1;31m{}\033[m'.format(a, b))
# cores no format
nome = 'David'
print('É um prazer te conheçer {}{}{}!!!'.format('\033[1;31m', nome, '\033[m'))
# outra forma
cores = {'limpa': '\033[m',
        'vermelho': '\033[31m',
         'verde': '\033[32m'}
print('Prazer em te conheçer {}{}{}'.format(cores['verde'], nome, cores['limpa']))
