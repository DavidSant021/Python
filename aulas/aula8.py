from math import sqrt, ceil, floor
rq = int(input('Digite um nùmero pra obter a raíz quadrada:'))
raiz = sqrt(rq)
print('A raíz quadrada de {}\n Exata é = {:.2f}\n Para mais = {}\n Para menos = {}'.format(rq, raiz, ceil(raiz), floor(raiz)))
