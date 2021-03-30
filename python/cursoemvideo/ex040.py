n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1+n2) / 2
if media >= 7:
    print(f'Sua média é de {media:.1f}: Você foi APROVADO!')
elif media >= 5:
    print(f'Sua media é de {media:.1f}: Você está de RECUPERAÇÃO!')
else:
    print(f'Sua média é de {media:.1f}: Você foi REPROVAD!')