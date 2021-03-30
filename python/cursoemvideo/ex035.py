a = float(input('Digite a reta 1: '))
b = float(input('Digite a reta 2: '))
c = float(input('Digite a reta 3: '))
if a + b > c and a + c > b and b + c > a:
    print('As retas apresentadas podem formar um triângulo.')
else: print('As retas apresentadas não podem formar um triângulo.')
