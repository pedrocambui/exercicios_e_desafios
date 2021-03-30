n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
ctrl = 6
while ctrl != 5:
    print('''O que você quer fazer?
    [1] SOMAR
    [2] MULTIPLICAR
    [3] MAIOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA''')
    ctrl = int(input('Opção: '))
    if ctrl == 1:
        print(f'A soma dos dois valores é {n1+n2}')
    elif ctrl == 2:
        print(f'A multiplicação dos dois valores é {n1*n2}')
    elif ctrl == 3:
        if n1 == n2:
            print('Os dois valores são iguais.')
        if n1 > n2:
            print(f'O maior valor presentado foi {n1}')
        elif n2 > n1:
            print(f'O maior valor apresentado foi {n2}')
    elif ctrl == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida. Tente novamente.')
    print('=' * 28)
print('FIM do programa.')