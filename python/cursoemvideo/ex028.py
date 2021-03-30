from random import randint
n = int(input('Digite um nímero inteiro entre 0 e 5: '))
npc = randint(0, 5)
if n == npc:
    print('PARABÉNS! Você acertou !')
else:
    print('QUE PENA. Você errou.. tente novamente.')