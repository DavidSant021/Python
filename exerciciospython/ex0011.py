#Converter área em mt quadrado e saber qnd gasta de tinta#
l = float(input('Qual a largura da parede?'))
a = float(input('Qual a altura da parede?'))
m2 = (l*a)
lt = (m2/2)
print('A sua parede tem a dimensão de {}x{} e com isso possui {:.2f}m² e gastará {:.2f}l de tinta.'.format(l, a, m2, lt))
