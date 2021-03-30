cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Foram digitados {cont} números. E a soma entre eles é {soma}')