soma = 0
cont = 0
for c in range (0,500, 3):
    if c % 2 == 1:
        soma += c
        cont +=1
        print(c)
print(f'A soma de todos os {cont} valores solicitados é {soma}')