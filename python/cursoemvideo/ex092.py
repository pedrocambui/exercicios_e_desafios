from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
pessoa['idade'] = date.today().year - nasc
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    salario = float(input('Salario: '))
    pessoa['salario'] = salario
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - date.today().year + pessoa['idade']
for k, v in pessoa.items():
    if k == 'salario':
        print(f'{k}: R${v:.2f}')
    else:
        print(f'{k}: {v}')