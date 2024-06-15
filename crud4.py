import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'PIZZARIA'
)

cursor = conexao.cursor()
NOME = "Fanta"
comando = f'DELETE FROM BEBIDA WHERE NOME = "{NOME}"'
cursor.execute(comando)
conexao.commit()