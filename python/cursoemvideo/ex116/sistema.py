from ex116.lib.interface import *
from ex116.lib.arquivo import *

arquivoExiste('arquivopc.txt')

while True:
    cabeçalho('MENU PRINCIPAL')
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        mostrarArquivo('arquivopc.txt')
    elif resposta == 2:
        nome = str(input('Nome: ')).strip()
        idade = leiaint('Idade: ')
        adicionaArquivo('arquivopc.txt', nome, idade)
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção valida!')
