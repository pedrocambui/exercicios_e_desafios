ex = str(input('Digite a expressão: '))
lista = list()
for c in ex:
    if c == '(':
        lista.append('(')
    if c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão é valida!')
else:
    print('Sua expressão não é valida! Ta errado carai!')
