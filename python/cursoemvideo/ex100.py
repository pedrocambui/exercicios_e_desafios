from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        print(f'{n}', end=' ')
        sleep(0.5)
        lista.append(n)
    print('PRONTO!')


def somapar(lst):
    soma = 0
    for v in lst:
        if v % 2 ==0:
            soma += v
    print(f'Somando os valores pares de {lst}, temos {soma}.')


numeros = list()
sorteia(numeros)
somapar(numeros)
