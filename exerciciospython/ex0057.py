s = str(input('Informe seu sexo: [M/F] ')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('Opção invalida. Informe seu sexo Novamente: [M/F] ')).upper()[0].strip()
print('Sexo {} registrado com sucesso. '.format(s))
