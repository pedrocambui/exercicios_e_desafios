tupla = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')
n = int(input('Digite um número entre 0 e 20: '))
while n not in range(0, 21):
    n = int(input('Digite um número entre 0 e 20: '))
print(tupla[n])