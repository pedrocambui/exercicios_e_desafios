from random import randint
npc = randint(0, 10)
acertou = False
cont = 0
while not acertou:
    n = int(input('Digite um número entre 0 e 10: '))
    if n == npc:
        acertou = True
    cont += 1
    print(npc)
print(f'PARABÉNS! Você acertou ! Foram necessarias {cont} tentativas.')
