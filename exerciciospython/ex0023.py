# Saber a unidade, dezena, centena e milhar de um número
n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando seu número...\nUnidade {}\nDezena {}\nCentena {}\nMilhar {}'.format(u, d, c, m))
