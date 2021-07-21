import sqlite3
import re

#obtendo fonte de dados
addr = input("Insira o nome da fonte de dados: ")
try: file = open(addr)
except: print("Arquivo não encontrado"); exit()

#criando conexão com a base de dados
conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

#verificando / limpando base atual e criando tabelas
cur.execute("DROP TABLE IF EXISTS Counts") #elimina a tabela Counts, se já existir
cur.execute("CREATE TABLE Counts (org TEXT, count INTEGER)") #cria uma nova tabela Counts com duas colunas (org e count)

#lendo fonte de dados 
print("Trabalhando...", end="")
i =  0
for line in file:
    if not line.startswith("From: "): continue #se a linha não começar com "From: ", pule
    if i == 500: #a cada 500 entradas encontradas
        conn.commit() #escreva as informações no banco de dados
        print(".", end="")
        i = 0
    parts = line.split() #divida a linha em uma lista de strings usando " " como delimitador
    email = parts[1]
    domain = list()
    domain.extend(re.findall(".*@(.+)", email)) # cria uma variável domain que contém todas as occorências de "*@*""
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain[0],)) #busca uma linha que contenha o valor de domain
    row = cur.fetchone()
    if row is None: #se não existir, crie uma e defina o valor de count para 1 
        cur.execute("INSERT INTO Counts (org, count) VALUES (?, 1)", (domain[0],))
    else: #se existir, adicione um ao valor de count
        cur.execute("UPDATE Counts SET count = count + 1 WHERE org = ?",(domain[0],))
    i += 1

conn.commit()
print("\nOs dez domínios mais comuns na fonte de dados são:")
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(str(row[0]), str(row[1]))
cur.close 

