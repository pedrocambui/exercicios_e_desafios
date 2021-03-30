lista = [[], []]
for c in range(0, 7):
    n = (int(input(f'Digite o {c+1}º valor: ')))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print(f'Os números pares digitados em ordem crescente é : {sorted(lista[0])}')
print(f'Os números pares impares em ordem crescente é : {sorted(lista[1])}')
print(lista)