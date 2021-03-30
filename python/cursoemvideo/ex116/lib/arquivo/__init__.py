def arquivoExiste(arq):
    try:
        a = open('arquivopc.txt', 'rt')
        a = a.close()
    except FileNotFoundError:
        a = open('arquivopc.txt', 'wt+')
        a = a.close()


def mostrarArquivo(arq):
    a = open(arq, 'rt')
    lista = a.readlines()
    for linha in lista:
        linha.split(';')
        print(linha)
    a = a.close


def adicionaArquivo(arq, nome, idade):
    a = open(arq, 'r')
    conteudo = a.readlines()
    conteudo.append(f'{nome};{idade}\n')
    a = open(arq, 'w')
    a.writelines(conteudo)
    a = a.close()
