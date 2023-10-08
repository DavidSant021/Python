#Medir hipotenusa#
from math import hypot
op = float(input('Qual o comprimento do cateto oposto?'))
ad = float(input('Qual o comprimento do cateto adjacente?'))
print('A hipotenusa mais medir: {:.2f}'. format(hypot(op, ad)))
