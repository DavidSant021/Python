lista1 = list()
lista1.append('David')
lista1.append(21)
lista2 = list()
lista2.append(lista1[:])
lista1[0] = 'Ester'
lista1[1] = 17
lista2.append(lista1[:])
print(lista2)
