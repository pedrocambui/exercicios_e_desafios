lista = list()
while True:
    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
    continuar = str(input('Quer continuar? [S/N]: ')).strip()
    if continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]: ')).strip()
    if continuar[0] in 'nN':
        break
print(f'{sorted(lista)}')