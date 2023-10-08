from time import sleep
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0
while opcao != 5:
    print('\033[1;36m=-=\033[m' * 25)
    print('''\033[1;32m>>>Opções:<<<\033[m
\033[1;42m[1] Somar\033[m
\033[1;43m[2] Multiplicar\033[m
\033[1;46m[3] Maior\033[m
\033[1;40m[4] Novos Números\033[m
\033[1;41m[5] Sair do programa\033[m''')
    print('\033[1;36m=-=\033[m' * 25)
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('A soma de {} e {} é igual a {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação de {} por {} é igual a {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os valores novamente.')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando o programa...')
        sleep(2)
    else:
        print('Opção invalida tente novamente.')
print('Programa finalizado')
