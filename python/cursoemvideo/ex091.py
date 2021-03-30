from random import randint
from time import sleep
from operator import itemgetter
game = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
ranking = list()
print('Valores sorteados: ')
for k, v in game.items():
    print(f'   O {k} tirou {v}')
    sleep(0.8)
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print(f'{"== RANKING DOS JOGADORES ==":^50}')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: O {v[0]} com {v[1]}')
    sleep(0.8)
