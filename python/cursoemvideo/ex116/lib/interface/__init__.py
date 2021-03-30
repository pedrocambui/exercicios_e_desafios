def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c +=1
    opc = leiaint('Sua opção: ')
    return opc
