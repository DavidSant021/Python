from time import sleep


def lin():
    print('-=' * 25)


def maior(* num):
    lin()
    total = maio = 0
    print('Analisando os valores passados...')
    for n in num:
        print(f'{n} ', end='')
        sleep(0.3)
        if total == 0:
            maio = n
        else:
            if n > maio:
                maio = n
        total += 1
    print(f'Foram informados {total} valores ao todo.')
    print(f'O maior valor informado foi {maio}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
