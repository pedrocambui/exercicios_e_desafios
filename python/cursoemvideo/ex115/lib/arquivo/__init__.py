from ex115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a = a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criaarquivo(nome):
     a = open(nome, 'wt+')
     a = a.close()


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<28}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('ERRO ao tentar escrever no arquivo!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
