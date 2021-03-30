sexo = str(input('Sexo [M/F]: ')).strip()
while sexo not in 'MmFf':
    print('Opção inválida.')
    sexo = str(input('Porfavor informe seu sexo [M/F]: ')).strip()

