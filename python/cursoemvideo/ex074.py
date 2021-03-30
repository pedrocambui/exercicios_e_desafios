from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os valores sorteados foram: ', end='')
for t in tupla:
    print(f'{t} ', end='')
print(f'\nO maior valor sorteado foi {max(tupla)}')
print(f'O menor valor sorteado foi {min(tupla)}')


"""from random import randint
tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
c = maior = menor =0
while c <= 4:
    if c == 0:
        maior =tupla[c]
        menor = tupla[c]
    if tupla[c] > maior:
        maior = tupla[c]
    if tupla[c] < menor:
        menor = tupla[c]
    c += 1
print(f'Os valores sorteados foram: ', end='')
for t in tupla:
    print(f'{t} ', end='')
print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')"""
