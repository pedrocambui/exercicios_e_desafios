n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3
print(f'O maior número digitado foi: {maior}')
print(f'O menor número digitado foi: {menor}')
"""if n1 > n2 and n1 > n3:
    print(f'O maior numero digitado foi: {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior numero digitado foi: {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior número digitado foi: {n3}')
if n1 < n2 and n1 < n3:
    print(f'O menor numero digitado foi: {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor numero digitado foi: {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor número digitado foi: {n3}')"""
