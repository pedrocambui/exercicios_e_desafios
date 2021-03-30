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
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return num
