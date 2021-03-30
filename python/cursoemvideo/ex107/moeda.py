def metade(num):
    """
    -> Encontra a metade de um número.
    :param num: Número a ser dividido.
    :return: Metade
    """
    n = num / 2
    return n


def dobro(num):
    """
    -> Encontra o dobro de um número.
    :param num: Número que será multiplicado.
    :return: Dobro.
    """
    n = num * 2
    return n


def aumentar(num, taxa):
    """
    -> Aumenta um valor em determinada porcentagem.
    :param num: Valor.
    :param taxa: Porcentagem a ser aumentada em %.
    :return: Valor + Taxa%
    """
    n = num + num * (taxa / 100)
    return n


def diminuir(num, taxa):
    """
    -> Diminui um valor em determinada porcentagem.
    :param num: Valor.
    :param taxa: Porcentagem a ser diminuida. %.
    :return: Valor -%Taxa
    """
    n = num - num * (taxa / 100)
    return n

