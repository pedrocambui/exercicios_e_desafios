matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
        if matriz[l][c] == matriz[1][0]:
            maior = matriz[l][c]
        else:
            if matriz[1][c] > maior:
                maior = matriz[1][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {par}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {maior}')