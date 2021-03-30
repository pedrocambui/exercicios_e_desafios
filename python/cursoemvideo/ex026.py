frase = str(input('Digite uma frase: ')).lower().strip()
print(f'Nessa frase a letra "A" aparece {frase.count("a")} vezes.')
print(f'A letra "A" aparece pela primeira vez na posição {frase.find("a")+1}.')
print(f'A ultima letra "A" apareceu na posição {frase.rfind("a")+1}')
