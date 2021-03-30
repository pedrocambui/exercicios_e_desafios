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
