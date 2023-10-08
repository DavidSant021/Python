desempenho = dict()
desempenho['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
listg = list()
for p in range(1, partidas + 1):
    listg.append(int(input(f'   Quantos gols na partida {p}? ')))
desempenho['gols'] = listg
desempenho['total'] = sum(listg)
print('-=' * 35)
print(desempenho)
print('-=' * 35)
for k, v in desempenho.items():
    print(f'O campo {k} tem o valor de {v}.')
print('-=' * 35)
print(f'O jogador {desempenho["nome"]} jogou {len(desempenho["gols"])} partidas.')
for i, pt in enumerate(desempenho['gols']):
    print(f'   => Na partida {i+1}, fez {pt} gols.')
print(f'Foi um total de {desempenho["total"]} gols.')
