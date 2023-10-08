r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR UM TRIÂNGULO.')
    if r1 == r2 == r3:
        print('É um triângulo EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('É um triângulo ISÓSCELES.')
    else:
        print('É um triângulo ESCALENO.')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR UM TRIÂNGULO.')
# elif r1 != r2 != r3 != r1 escaleno pois todos são diferentes
