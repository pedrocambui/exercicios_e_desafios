homens = maior = mulheres = 0
continuar = sexo = ' '
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade > 18:
        maior += 1
    sexo = str(input('Sexo: [M/F]')).strip().lower()[0]
    while sexo not in 'mf':
        sexo = str(input('Sexo: [M/F]')).strip().lower()[0]
    if sexo == 'm':
        homens += 1
    if sexo == 'm' and idade < 20:
        mulheres += 1
    print('-' * 30)
    continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if continuar == 'n':
        break
print('\n==== FIM DO PROGRAMA ====')
print(f'Total de pessoas com mais de  18 anos: {maior}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres} mulheres com menos de 20 anos.')