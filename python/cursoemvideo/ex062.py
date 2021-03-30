print('='*19)
print('10 TERMOS DE UMA PA')
print('='*19)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razâo: '))
termo = primeiro
cont = 1
mais = 1
ultimo = 10
while mais != 0:
    while cont <= ultimo:
        print(f'{termo} >', end='')
        termo += razao
        cont +=1
    print(' PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    ultimo += mais
print('FIM')

