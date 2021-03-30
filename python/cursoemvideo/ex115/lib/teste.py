"""def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(f'{txt:^42}')
    print(linha())


def menu(*opc):
    while True:
        cabeçalho('MENU PRINCIPAL')
        print('\033[1;33m1\033[m - \033[1;34mVer pessoas cadastradas\033[m')
        print('\033[1;33m2\033[m - \033[1;34mCadastrar nova Pessoa\033[m')
        print('\033[1;33m3\033[m - \033[1;34mSair do Sistema\033[m')
        try:
            opc = int(input('\033[1;33mSua opção: \033[m'))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        if opc == 1:
            cabeçalho('Opção 1')
        elif opc == 2:
            cabeçalho('Opção 2')
        elif opc == 3:
            break
        else:
            print('\033[31mERRO!Digite uma opção válida!.\033[m')
"""