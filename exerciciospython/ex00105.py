def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param num: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    cadastro = dict()
    cadastro['total'] = len(num)
    cadastro['maior'] = max(num)
    cadastro['menor'] = min(num)
    cadastro['média'] = sum(num) / len(num)
    if sit:
        if cadastro['média'] >= 7:
            cadastro['situação'] = 'BOA'
        if 5 < cadastro['média'] < 7:
            cadastro['situação'] = 'RAZOÁVEL'
        if cadastro['média'] <= 5:
            cadastro['situação'] = 'RUIM'
    print('_' * 70)
    return cadastro


#  Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
for k, v in resp.items():
    print(f'O campo {k} tem o valor {v}')
