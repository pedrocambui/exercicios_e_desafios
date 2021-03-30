def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! {entrada} é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[0;31mERRO! Por favor, digite um número inteiro válido.\033[m')
            continue
        else:
            return n

