peso = float(input('Peso: '))
altura =  float(input('Altura: '))
imc = peso / (altura*altura)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}. Você está a BAIXO do peso.')
elif imc < 25:
    print(f'Seu IMC é de {imc:.1f}. Você está no peso IDEAL.')
elif imc < 30:
    print(f'Seu IMC é de {imc:.1f}. Você está com SOBREPESO.')
elif imc < 40:
    print(f'Seu IMC  é de {imc:.1f}. Você está com OBESIDADE.')
else:
    print(f'Você está com OBESIDADE MÓRBIDA.')