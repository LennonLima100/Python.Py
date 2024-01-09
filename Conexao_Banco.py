# Importação
import pyodbc

#Função de Retornar Conexão
def retornar_conexao_sql():
	server = 'NOME SERVIDOR'
	database = 'NOME BANCO DE DADOS'
	username = 'LOGIN'
	password = 'SENHA'
	driver = '{OBDC Driver 17 for SQL Server}'
	string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    conexao = pyodbc.connect (string_conexao)
    return conexao.cursor()
    
#Variável de Cursor
cursor = retornar_conexao_sql()

# Seleção de Dados no Banco
cursor.execute("FAZER O SELECT DESEJADO NO BANCO")
row = cursor.fetchone()
if row:
    print(row)

# teste
