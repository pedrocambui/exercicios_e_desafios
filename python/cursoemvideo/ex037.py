n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADESSIMAL''')
base = int(input('Sua opção:'))
if base == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')

elif base == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')

elif base == 3:
    print(f'{n} convertido para HEXADESSIMAL é igual a {hex(n)[2:]}')
else:
    print('Opção invalida.')
