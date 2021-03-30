lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Quer continuar? [S/N] ')).strip()
    if continuar [0] not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N] ')).strip()
    if continuar[0] in 'Nn':
        break
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'Os números digitados foram: {lista}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')
