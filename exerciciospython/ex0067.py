from time import sleep
while True:
    print('Digite números negativos para finalizar o programa.')
    v = int(input('Quer ver a tabuada de qual valor? '))
    if v < 0:
        break
    print('=' * 50)
    for c in range(1, 11):
        print(f'{v} x {c:2} = {v * c}')
    print('=' * 50)
print('=' * 50)
print('Finalizando Programa...')
sleep(2)
print('=' * 50)
print('Programa de tabuada finalizado.')
