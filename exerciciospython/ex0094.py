dados = dict()
lista = list()
somidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if dados['sexo'] in 'MmFf':
            break
        print('Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    somidade += dados['idade']
    lista.append(dados.copy())
    while True:
        op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if op in 'SsNn':
            break
        print('ERRO! Responda apenas S ou N.')
    if op in 'Nn':
        break
media = somidade / len(lista)
print('-=' * 30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.0f} anos.')
print(f'C) A(s) mulher(es) cadastradas foram:', end=' ')
for i in lista:
    if i['sexo'] in 'Ff':
        print(f'{i["nome"].capitalize()}', end=' ')
print()
print('D) Lista das pessoas que estão acima da média: ')
for i in lista:
    if i['idade'] >= media:
        print('   ', end='')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
