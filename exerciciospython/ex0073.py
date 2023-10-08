times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo',
         'Fluminense', 'Bragantino', 'Atlético PR',
         'Fortaleza', 'Atlético MG', 'Cuiabá', 'São Paulo',
         'Chapecoense', 'Cruzeiro', 'Corinthians',
         'Goiás', 'Bahia', 'Santos', 'Vasco', 'Coritiba', 'América MG')
print('=-=' * 20)
print(f'\033[1;32mLista de times do Brasileirão:\033[m {times}')
print('=-=' * 20)
print(f'\033[1;32mOs 5 primeiros colocados são:\033[m {times[0:5]}')
print('=-=' * 20)
print(f'\033[1;32mOs ultimos 4 colocados são:\033[m {times[-4:]}')
print('=-=' * 20)
print(f'''\033[1;32mOs times em ordem alfabética são:\033[m
{sorted(times)}''')
print('=-=' * 20)
print(f'\033[1;32mA Chapecoense esta na posição:\033[m {times.index("Chapecoense")+1}')
