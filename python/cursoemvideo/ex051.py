print('='*19)
print('10 TERMOS DE UMA PA')
print('='*19)
termo = int(input('Primeiro termo: '))
r = int(input('Razâo: '))
for c in range(termo, termo+10*r, r):
    print(f'{c} >', end=' ')

