from time import sleep


def contador(i, f, p):
    print('-='*20)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}: ')
    sleep(1.5)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += p
    else:
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= p
    print('FIM')


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
