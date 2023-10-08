r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos {}, {} e {} podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('Os seguimentos {}, {} e {} não podem formar um triângulo.'.format(r1, r2, r3))
