maior = 0
menor = 0
for c in range(0, 5):
    peso = float(input('Digite o peso em kg: '))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior:}Kg. E o menor foi de {menor}Kg.')