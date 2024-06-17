import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'PIZZARIA'
)

cursor = conexao.cursor()
comando = 'SELECT * FROM BEBIDA'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

cursor.close()
conexao.close()