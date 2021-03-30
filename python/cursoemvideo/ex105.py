def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['média'] = sum(num) / len(num)
    if sit:
        if aluno['média'] >= 7:
            aluno['situação'] = 'BOA'
        elif 5 <= aluno['média'] < 7:
            aluno['situação'] = 'RAZOÁVEL'
        else:
            aluno['situação'] = 'RUIM'
    return aluno


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
