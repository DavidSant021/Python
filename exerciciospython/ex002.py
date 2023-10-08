n1 = int(input('Qual primeiro número? '))
n2 = int(input('Qual é o segundo número da soma?'))
s = (n1+n2)
print('A soma entre \033[1;35m{0}\033[m e \033[1;36m{1}\033[m equivale a \033[4;32m{2}\033[m.' .format(n1, n2, s))
