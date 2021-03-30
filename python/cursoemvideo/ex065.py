n = maior = media = cont = soma = 0
menor = 10000
continuar = 's'
while continuar[0] in 'sS':
    n = int(input('Digite um numero: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    cont += 1
    continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()
    if continuar[0] not in 'sSnN':
        print('Opção inválida. Tente novamente.')
        continuar = str(input('Quer continuar? [S/N]: ')).strip().lower()
print(f'Foram digitados {cont} valores sendo que o maior número digitado foi {maior} e o menor foi {menor}.')
print(f'E a média entre os números digitados é {soma/cont:.1f}')