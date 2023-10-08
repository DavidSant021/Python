op = 0
while op != 5 or op == 4:
    print('''\033[1;32mOpções:\033[m
       \033[1;42m[1] Somar\033[m
       \033[1;43m[2] Multiplicar\033[m
       \033[1;46m[3] Maior\033[m
       \033[1;40m[4] Novos Números\033[m
       \033[1;41m[5] Sair do programa\033[m''')
    print('\033[1;35m-=\033[m' * 25)
    op = int(input('\033[1;32mEscolha uma opção:\033[m '))
    print('\033[1;35m-=\033[m' * 25)
    n1 = int(input('\033[1;32mDigite um número:\033[m '))
    n2 = int(input('\033[1;32mDigite um número:\033[m '))
    if op == 1:
        print('\033[1;32mA soma de {} e {} é igual a {}\033[m'.format(n1, n2, n1 + n2))
        print('\033[1;35m-=\033[m' * 25)
    if op == 2:
        print('\033[1;33mA multiplicação de {} por {} é igual a {}\033[m'.format(n1, n2, n1 * n2))
        print('\033[1;35m-=\033[m' * 25)
    if op == 3:
        if n1 > n2:
            print('\033[1;36mO maior valor é {}\033[m'.format(n1))
            print('\033[1;35m-=\033[m' * 25)
        else:
            print('\033[1;36mO maior valor é {}\033[m'.format(n2))
            print('\033[1;35m-=\033[m' * 25)
