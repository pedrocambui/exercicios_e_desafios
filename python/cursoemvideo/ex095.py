jogador = {}
jogadores = list()
gols = list()
cont = 0
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'  Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
        if continuar in 'sn':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'n':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    lev = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if lev == 999:
        break
    if lev > len(jogadores):
        print(f'ERRO! Não existe jogador com o código {lev}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[lev]["nome"]} --')
        for i, v in enumerate(jogadores[lev]['gols']):
            print(f'   No jogo {i+1} fez {v} gols.')
        print('-='*30)