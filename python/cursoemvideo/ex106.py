from time import sleep
c = ('\033[m',        # 0 - sem cores
     '\033[0;97;41m',  # 1 - vermelho
     '\033[1;97;42m',  # 2 - verde
     '\033[0;97;43m',  # 3 - amarelo
     '\033[0;97;44m',  # 4 - azul
     '\033[0;97;45m',  # 5 - roxo
     '\033[7;97m'     # 6 - branco
     );


def ajuda(com):
    escreva(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def escreva(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)
    print(c[0], end='')
    sleep(1)


comando = ''
while True:
    escreva('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando == 'fim':
        break
    else:
        ajuda(comando)
escreva('ATÉ LOGO!', 1)

