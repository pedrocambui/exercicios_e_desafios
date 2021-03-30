valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
financiamento = valor / (anos*12)
porcentagem = salario*0.30
if financiamento >= porcentagem:
    print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${financiamento:.2f}. Empréstimo NEGADO!')
else:
    print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${financiamento:.2f}. Empréstimo pode ser CONCEDIDO!')
