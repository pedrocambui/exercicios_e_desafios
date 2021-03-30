print('='*30)
print('SEQUÊNCIA DE FIBONACCI')
print('='*30)
n = int(input('Quantos termos você quer mostrar? '))
cont = 0
a = 0
b = 1
c = a + b
while cont < n:
    print(f'{a} >', end=' ')
    a = b
    b = c
    c = a + b
    cont += 1
print('FIM')