def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def line(tam=42):
    return '-' * 42


def header(txt):
    print(line())
    print(txt.center(42))
    print(line())


def menu(lista):
    header('SISTEMA PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[33m{cont}\033[m - \033[34m{item}\033[m')
    line()
    opc = leiaint('\033[33mSua opção:\033[m ')
    return opc
