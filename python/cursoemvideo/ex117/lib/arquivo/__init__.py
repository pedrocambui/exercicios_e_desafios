from ex117.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def arquivoCriar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO ao criar o arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def arquivoLer(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um ERRO ao ler o arquivo.')
    else:
        header('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} cadastrado com sucesso.')
            a.close()

