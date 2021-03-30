produto = float(input('Valor do produto: R$'))
print('''Qual será a forma de pagamento?
[ 1 ] À vista com 10% de desconto.
[ 2 ] À vista no cartão com 5% de desconto.
[ 3 ] Em até 2x sem juros.
[ 4 ] 3x ou mais com 20 % de juros.''')
cond = int(input('Selecione: '))
if cond == 1:
    valor = produto - (produto*0.10)
    print(f'À vista o produto sairá por R${valor:.2f}')
elif cond == 2:
    valor = produto - (produto*0.05)
    print(f'À vista no cartão o produtor sairá por R${valor:.2f}')
elif cond == 3:
    print(f'Em até 2x no cartão o produto sem juros sairá por R${produto:.2f}')
elif cond == 4:
    parcelas = int(input('Quantas parcelas?'))
    valor = produto + (produto*0.20)
    print(f'Sua compra será parcelada em {parcelas} de R${valor/parcelas:.2f}')
    print(f'Em 3x ou mais no cartão o produto sairá por {valor:.2f}')
else:
    print('Opção inválida.')