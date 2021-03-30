from datetime import date

nasc = int(input('Ano de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print(f'O atleta tem {idade} anos e está na categoria MIRIM.')
elif idade <= 14:
    print(f'O atleta tem {idade} anos e está na categoria INFANTIL.')
elif idade <= 19:
    print(f'O atleta tem {idade} anos e está na categoria JUNIOR.')
elif idade <= 25:
    print(f'O atleta tem {idade} anos e está na categoria SÊNIOR.')
else:
    print(f'O atleta tem {idade} anos e está na categoria MASTER.')