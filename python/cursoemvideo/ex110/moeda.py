def metade(preço, formt=False):
    n = preço / 2
    if formt:
        return moeda(n)
    else:
        return n


def dobro(preço, formt=False):
    n = preço * 2
    if formt:
        return moeda(n)
    else:
        return n


def aumentar(preço=0, taxa=0, formt=False):
    n = preço + preço * (taxa / 100)
    if formt:
        return moeda(n)
    else:
        return n


def diminuir(preço=0, taxa=0, formt=False):
    n = preço - preço * (taxa / 100)
    if formt:
        return moeda(n)
    else:
        return n


def moeda(preço=0, moeda='R$', formt=False):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxad=5, formt=True):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxad}% de redução: \t{diminuir(preço, taxad, True)}')
    print('-' * 30)
