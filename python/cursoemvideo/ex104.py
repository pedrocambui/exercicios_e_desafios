def leiaint(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            break
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')