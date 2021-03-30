from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade = date.today().year - nascimento
falta = 18 - idade

if idade < 18:
    print(f'''Quem nasceu em {nascimento} faz {idade} anos em {date.today().year}.
Ainda faltam {falta} anos para o alistamento.
seu alistamento será em {nascimento+18}''')

elif idade > 18:
    print(f'''Quem nasceu em {nascimento} faz {idade} anos em {date.today().year}.
Você já deveria ter se alistado há {idade-18} anos.
Seu alistamento foi em {nascimento+18}.''')

else:
    print(f'''Quem nasceu em {nascimento} faz {idade} anos em {date.today().year}.
Você tem que se alistar IMEDIATAMENTE!''')
