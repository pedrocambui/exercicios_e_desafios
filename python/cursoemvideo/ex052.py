n = int(input('Digite um número: '))
cont = 0
div = 0
for c in range(2, n+1):
    div = n%c
    if div == 0:
        cont +=1
if cont == 1:
    print('O numero é primo!')
else:
    print('O numero não é primo')


