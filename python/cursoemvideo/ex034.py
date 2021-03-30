sal = float(input('Digite seu salario: R$'))
if sal <= 1250:
    print(f'Seu salario com 15 % de aumento será de {sal + (sal * 0.15)}')
else:
    print(f'Seu salario com 10 % de aumento será de {sal + (sal * 0.10)}')
