frase = str(input('Digite uma frase: ')).strip().lower().split()
frase = ''.join(frase)
if frase[::-1] == frase:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')