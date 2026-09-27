
import mysql.connector
import pandas as pd

# 1. Configuração da conexão com o banco local
conexao = mysql.connector.connect(
    host="localhost",
    user="elidados",       # Substitua pelo seu usuário do MySQL (ex: root)
    password="270291elias",     # Substitua pela sua senha do MySQL
    database="projeto_sql"
)

cursor = conexao.cursor()
print("Conexão com o banco 'projeto_sql' realizada com sucesso!")

#


# Fechando as conexões ao final do script
cursor.close()
conexao.close()












