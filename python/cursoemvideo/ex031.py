km = float(input('Digite a distância da viajem em KM: '))
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print(f'Para sua viagem de {km}KM será o cobrado R${valor}')