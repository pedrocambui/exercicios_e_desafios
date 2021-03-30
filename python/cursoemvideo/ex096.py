def area(l, c):
    a = l * c
    print(f'A area de um terreno {l}x{c} é de {a}m².')

print(' Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('CUMPRIMENTO (m): '))
area(l, c)