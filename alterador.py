import pyodbc 
import pandas as pd

#Conexão com servidor
conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=SERVIDOR;'                      
                        'Database=DATABASE;'
                        'UID=USERNAME;'
			'PWD=PASSWORD;'                     
                        'Trusted_Connection=yes;')
cursor = conn.cursor()

escolha = 'S'

print("Alterar status de nota por chave!\n")

while(escolha != 'N'):
    #entrada de dados a serem alterados
    nota = input("Digite o numero da chave fato a ser alterada: ")

    #Apresentação de como está atualmente no servidor
    print("\n")
    df = pd.read_sql(r"select status_nfe, * from tbSaidas where Chave_fato = '{}'".format(nota),conn)
    print(df)

    #entrada de dados a serem alterados
    status = input("Qual status deseja colocar na nota? (A ou N) ")

    #código gerado a partir dos dados fornecidos
    print("\n")
    sql = "update tbSaidas set status_nfe = '{}' where Chave_fato = '{}'".format(status, nota)
    print(sql)
    print("\n")

    #execução e commit
    conn.execute(sql)
    conn.commit()

    print("Nota atualizada!\n")

    #Apresentação de como está após atualização no servidor
    df = pd.read_sql(r"select status_nfe, * from tbSaidas where Chave_fato = '{}'".format(nota),conn)
    print(df)
    print("\n")

    escolha = input("Deseja fazer outra operação? [S/N] ")
    escolha.upper()
    print("\n")
