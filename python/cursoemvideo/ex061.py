print('='*19)
print('10 TERMOS DE UMA PA')
print('='*19)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} >', end='')
    termo += razao
    cont += 1
print('FIM')