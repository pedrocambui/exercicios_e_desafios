lista = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip(). lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de: ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {menor}kg. Peso de: ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')

"""lista = list()
dados = list()
pesados = list()
leves = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(lista) == 0:
        pesados.append(dados[:])
        leves.append(dados[:])
    else:
        if dados[1] == pesados[0][1]:
            pesados.append(dados[:])
        elif dados[1] > pesados[0][1]:
            pesados.clear()
            pesados.append(dados[:])
        if dados[1] == leves[0][1]:
            leves.append(dados[:])
        elif dados[1] < leves[0][1]:
            leves.clear()
            leves.append(dados[:])
    lista.append(dados[:])
    dados.clear()
    continuar = str(input('Quer continuar? [S/N]')).strip(). lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
print('-='*30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'Os maiores pesos foram de: {pesados}')
print(f'Os menores pesos foram de {leves}')"""