def metade(preço):
    """
    -> Encontra a metade de um número.
    :param num: Número a ser dividido.
    :return: Metade
    """
    n = preço / 2
    return n


def dobro(preço):
    """
    -> Encontra o dobro de um número.
    :param num: Número que será multiplicado.
    :return: Dobro.
    """
    n = preço * 2
    return n


def aumentar(preço=0, taxa=0):
    """
    -> Aumenta um valor em determinada porcentagem.
    :param num: Valor.
    :param taxa: Porcentagem a ser aumentada em %.
    :return: Valor + Taxa%
    """
    n = preço + preço * (taxa / 100)
    return n


def diminuir(preço=0, taxa=0):
    """
    -> Diminui um valor em determinada porcentagem.
    :param num: Valor.
    :param taxa: Porcentagem a ser diminuida. %.
    :return: Valor -%Taxa
    """
    n = preço + preço * (taxa / 100)
    return n


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')
