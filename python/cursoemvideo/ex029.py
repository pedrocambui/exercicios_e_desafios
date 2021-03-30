vel = int(input('Qual a velocidade do carro?: '))
if vel >= 80:
    multa = (vel -80) * 7
    print(f'Você está indo muito rapido e por isso foi multado em: R${multa:.2f}.')
