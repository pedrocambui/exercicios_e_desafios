total = mais = produtos = 0
barato = ' '
menor = 100000000000000
while True:
    nome = str(input('Nome do produto: ')).strip()
    valor = float(input('Preço do produto: R$'))
    if valor < menor:
        menor = valor
        barato = nome
    if valor > 1000:
        mais += 1
    total += valor
    continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    while continuar not in 'sn':
         continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break
print(f'O total gasto na compra foi de R${total:.2f}')
print(f'{mais} produtos custaram mais de R$ 1000.00')
print(f'E o produto mais barato foi {barato}')