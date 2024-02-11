import sqlite3

banco = sqlite3.connect('banco.db')
cursor = banco.cursor()

#criando o a tabela 
cursor.execute("CREATE TABLE alunos (id integer , nome text , cpf integer , endereco text , nome_mae text)")

#inserindo alunos na tabela
cursor.execute("INSERT INTO alunos VALUES (1,'Dulce',2395869295,'Rua Dulcem santos sp','Maria')")
cursor.execute("INSERT INTO alunos VALUES (2,'Henry',10957482,'Rua Santos 23 santos sp ','Lucia')")
cursor.execute("INSERT INTO alunos VALUES (3,'Maria',1868238503,'Rua Borges 101 ','Maria')")
cursor.execute("INSERT INTO alunos VALUES (4,'Ana',158736455,'Rua Santos Drumond 1355 estrada Santos ','Maria')")
cursor.execute("INSERT INTO alunos VALUES (6,'Claudia',1230973,'Rua barreto 24096 Santos ','Maria')")
cursor.execute("INSERT INTO alunos VALUES (7,'Julia',09175977,'Rua 23 de abril Santos ','Maria')")
cursor.execute("INSERT INTO alunos VALUES (8,'Taina',09097567,'Rua Matheus avenida dulce 68 Santos','Maria')")
cursor.execute("INSERT INTO alunos VALUES (9,'Gustavo',09800974,'Av andre de camargo Santos ','Maria')")

#mostrando os dados implementados na tabela
cursor.execute("SELECT * FROM alunos")
print(cursor.fetchall())
