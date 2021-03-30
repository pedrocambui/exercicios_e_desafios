print('=' *30)
print('{:^30}'.format('BANCO DO PC'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced =50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced +=1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break





"""cinquenta = vinte = dez = um = cont = 0
print('='*35)
print('BANCO DO PC')
print('='*35)
sacar = int(input('Qual será o valor sacado? R$'))
while sacar > 0:
    if sacar >= 50:
        sacar -= 50
        cinquenta += 1
    elif sacar >= 20:
        sacar -= 20
        vinte +=1
    elif sacar >= 10:
        sacar -= 10
        dez += 1
    elif sacar >= 1:
        sacar -=1
        um += 1
if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de R$50')
if vinte > 0:
    print(f'Total de {vinte} cédulas de R$20')
if dez > 0:
    print(f'Total de {dez} cédulas de R$10')
if um > 0:
    print(f'Total de {um} cédulas de R$1')
print('='*35)
print('Volte sempre ao BANCO DO PC! Tenha um bom dia!')"""