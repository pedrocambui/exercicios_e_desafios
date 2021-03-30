import math
n = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(n))
cos = math.cos(math.radians(n))
tan = math.tan(math.radians(n))
print(f'O ângulo de {n} tem o SENO de {seno:.2f}, COSSENO de {cos:.2f} e a tangente de {tan:.2f}')