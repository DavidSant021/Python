#Ler o seno e cosseno de um ângulo#
from math import cos, sin, tan, radians
a = float(input('Digite o ângulo que você deseja:'))
r = radians(a)
print('O ângulo de {:.0f} tem o:\nSENO de: {:.2f}\nCOSSENO de: {:.2f}\nTANGENTE de: {:.2f}'.format(a, sin(r), cos(r), tan(r)))
