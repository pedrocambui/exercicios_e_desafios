from ex117.lib.interface import *
from ex117.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    arquivoCriar(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        arquivoLer(arq)
    elif resposta == 2:
        header('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('Saindo do programa... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
