import sqlite3 as conector

conexao = None
cursor = None

try:
    conexao = conector.connect('./meu_banco.db')
    conexao.execute('PRAGMA foreign_keys = on')
    cursor = conexao.cursor()

    comando = '''SELECT Municipio.nome, Dengue.casos, Populacao.populacao
                    FROM Municipio
                    JOIN Dengue ON Municipio.codigo = Dengue.codigo
                    JOIN Populacao ON Municipio.codigo = Populacao.codigo
                    WHERE Dengue.ano=:ano AND Populacao.ano=:ano'''

    ano = {'ano': 2019}
    cursor.execute(comando, ano)

    registros = cursor.fetchall()
    print(registros[0])
    print(f'{"municipio":30} - {"casos":5} - {"populacao":9} - {"incidencia"}')
    for registro  in registros:
        incidencia = registro[1] / registro[2]
        print(f'{registro[0]:30} - {registro[1]:5} -  {registro[2]:9} - {incidencia:.6f}')

    conexao.commit()

except conexao.OperationalError as erro:
    print('Erro operacional', erro)

except conexao.DatabaseError as erro:
    print('Erro de database', erro)

finally:
    if conexao:
        cursor.close()
        conexao.close()

