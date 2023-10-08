fr = str(input('Digite uma palavra: ')).strip().upper()  # tirei espaços externos e botei em maiúsculo
pl = fr.split()  # separei as palavras em uma lista
jt = ''.join(pl)  # juntei tudo tirando espaços internos
inv = jt[::-1]
'''inv = ''
for lt in range(len(jt) - 1, -1, -1):
    inv += jt[lt]  # inverti a frase'''
print('O inverso de  {} é {}'.format(jt, inv))
if inv == jt:  # se a frase for igual ao inverso vai ser palíndromo
    print('Temos um palíndromo. ')
else:
    print('A frase não é um palíndromo ')
