from random import randint
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
gamer = int(input('Qual a sua jogada? '))
npc = randint(0, 2)
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('-=-'*9)
print(f'O computador escolheu {itens[npc]}')
print(f'O jogador escolheu {itens[gamer]}')
print('-=-'*9)

if npc == 0:
    if gamer == 0:
        print('EMPATOU!')
    elif gamer == 1:
        print('JOGADOR VENCE!')
    elif gamer == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Opção INVALÍDA!')

elif npc == 1:
    if gamer == 0:
        print('COMPUTADOR VENCE!')
    elif gamer == 1:
        print('EMPATOU')
    elif gamer == 2:
        print('JOGADOR VENCE')
    else:
        print('Opção INVALÍDA!')
elif npc == 2:
    if gamer == 0:
        print('JOGADOR VENCE')
    elif gamer == 1:
        print('COMPUTADOR VENCE')
    elif gamer == 2:
        print('EMPATOU')
    else:
        print('Opção INVALÍDA!')