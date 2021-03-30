pessoas = dict()
lista = list()
total = 0
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip()
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]')).lower().strip()[0]
        if continuar in 'sn':
             break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'n':
        break
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
for c in lista:
    total += c['idade']
media = total / len(lista)
print(f'B) A média de idade é de {media} anos.')
print('C) As mulheres cadastradas foram : ', end=' ')
for c in lista:
    if c['sexo'] == 'F':
        print(c['nome'], end='... ')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for c in lista:
    if c['idade'] >= media:
        for k, v in c.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')