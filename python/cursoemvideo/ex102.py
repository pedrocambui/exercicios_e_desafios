def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta.
    :return: O valor do Fatorial do número n.
    """
    f = 1
    c = n
    while c > 0:
        f *= c
        if show:
            print(c, end='')
            print(f' x ' if c > 1 else ' = ', end='')
        c -= 1
    return f


print(fatorial(5, True))
