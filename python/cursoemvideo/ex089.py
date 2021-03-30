ficha = list()
continuar = ''
cont = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]')).lower().strip()[0]
    while continuar not in 'sn':
        continuar = str(input('Quer continuar? [S/N]'))
    if continuar == 'n':
        break
    cont += 1
print('-='*50)
print(f'{"No.":<6}{"NOME":<14}{"MÉDIA"}')
print('-'*30)
for c, i in enumerate(ficha):
    print(f'{c:<5} {i[0]:<14} {i[2]:.1f}')
print('-'*30)
while True:
    alunos = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if alunos == 999:
        break
    print(f'{ficha[alunos][0]}        {ficha[alunos][1]}')
