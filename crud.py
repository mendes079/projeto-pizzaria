import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'PIZZARIA'
)

cursor = conexao.cursor()
ID_BEBIDA = 4
NOME = "Fanta"
PRECO = 15.00
TIPO = "Refrigerante"
comando = f'INSERT INTO BEBIDA (ID_BEBIDA, NOME, PRECO, TIPO) VALUES ({ID_BEBIDA}, "{NOME}", {PRECO}, "{TIPO}")'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()