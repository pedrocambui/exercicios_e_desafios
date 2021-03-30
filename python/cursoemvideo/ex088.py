from random import randint
from time import sleep
print('-'*30)
print('      JOGA NA MEGA SENA       ')
print('-'*30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print()
jogo = list()
n = 0
print('-=' *3, f'SORTEANDO {qtd} JOGOS', '-='*3)
print()
for c in range(0, qtd):
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
        else:
            while n in jogo:
                n = randint(1, 60)
    print(f'Jogo {c+1}: {sorted(jogo)}')
    jogo.clear()
    sleep(0.8)
print()
print('-='*5, '< BOA SORTE! >', '-='*5)

"""from random import randint
from time import sleep
print('-'*30)
print('      JOGA NA MEGA SENA       ')
print('-'*30)
qtd = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
jogos = list()
lista = list()
while tot <= qtd:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' *3, f'SORTEANDO {qtd} JOGOS', '-='*3)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.8)
print('-='*5, '< BOA SORTE! >', '-='*5)"""