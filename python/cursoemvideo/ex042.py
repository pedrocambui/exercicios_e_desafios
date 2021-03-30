a = float(input('Digite a reta 1: '))
b = float(input('Digite a reta 2: '))
c = float(input('Digite a reta 3: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and a ==c:
        print('As retas apresentadas PODEM FORMAR um triângulo EQUILÁTERO')
    elif a == b and a != c or a == c and a != b or b == c and b != a:
        print('As retas apresentadas PODEM FORMAR um triângulo ISÓSCELES')
    else:
        print('As retas apresentadas PODEM FORMAR um triângulo ESCALENO')
else: print('As retas apresentadas não podem formar um triângulo.')
