from math import hypot
x = float(input('Digite o cateto oposto: '))
y = float(input('Digite o cateto adjacente: '))
h = hypot(x, y)
print(f'Baseado nos valores fornecidos a hupotenusa do triangulo é: {h:.2f}')