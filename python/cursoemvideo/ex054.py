from datetime import date
maior = 0
menor = 0
for c in range(0,6):
    ano = int(input('Ano de nascimento: '))
    if ano <= date.today().year -18:
        maior += 1
    else:
        menor += 1
if menor != 0 and maior != 0:
    print(f'Das sete pessoas {maior} já atingiram a maioridade e  {menor} ainda não.')
elif menor != 0 and maior ==0:
    print(f'As sete pessoas ainda são de menor.')
else:
    print('Todas são de maior.')