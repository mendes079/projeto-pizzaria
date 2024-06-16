import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'PIZZARIA'
)

cursor = conexao.cursor()
NOME = "Fanta"
PRECO = 14
comando = f'UPDATE BEBIDA SET PRECO = {PRECO} WHERE NOME = "{NOME}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()