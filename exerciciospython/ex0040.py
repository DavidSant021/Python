n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
med = (n1 + n2) / 2
if 7 > med >= 5:
    print('Sua média é de \033[1;36m{:.1f}\033[m e você está em \033[1;36mRECUPERAÇÃO\033[m.'.format(med))
elif med < 5:
    print('Sua média é de \033[1;31m{:.1f}\033[m e  você esta \033[1;31mREPROVADO\033[m.'.format(med))
elif med >= 7:
    print('Sua média é de \033[1;32m{:.1f}\033[m e você está \033[1;32mAPROVADO\033[m.'.format(med))
