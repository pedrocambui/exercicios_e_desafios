tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
par = False
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        par = True
        if par == True:
            print(tupla[c], end=' ')

"""tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
par = False
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}º posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram: ', end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
"""