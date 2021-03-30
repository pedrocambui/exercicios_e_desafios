maior = 0
soma = 0
cont = 0
velho = ''
for c in range(1, 5):
    print('-'*5, f'{c}º PESSOA', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()
    soma += idade
    if sexo[0] == 'f' and idade < 20:
        cont += 1
    if sexo[0] == 'm' and idade > maior:
        maior = idade
        velho = nome
print(f'A média de idade do grupo é de {soma/4:.1f} anos')
print(f'O homem mais velho tem {maior} anos e se chama {velho}')
print(f'Ao todo são {cont} mulheres com menos de 20 anos.')