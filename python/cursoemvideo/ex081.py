lista = list()
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip()
    if continuar[0] not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip()
    if continuar in 'Nn':
        break
print(f'Foram digitados {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista de valores em ordem crescente é: {lista}')
if 5 in lista:
    print(f'O número 5 está na lista.E aparece pela primeira vez na posição {lista.index(5)}')
else:
    print(f'O número 5 não está na lista.')