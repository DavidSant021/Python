n = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} na sua frase.'.format(n.count('A')))
print('A primeira letra"A" apareceu na posição {}'.format(n.find('A')+1))
print('A ùltima letra "A" aparece na posição {}'.format(n.rfind('A')+1))
