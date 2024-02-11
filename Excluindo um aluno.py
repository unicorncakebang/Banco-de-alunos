cursor.execute("DELETE FROM alunos WHERE cpf = 12455788)")
banco.close() #fechamento do banco de dados
print("Dado removido com sucesso do banco") #mensagem de remoção de dado
#mostrar lista total  de alunos após a exclusão do dado /ou dados solicitados
cursor.execute("SELECT * FROM alunos")

#tratamento de erro , se caso houver algum problema durante a exclusão
except sqlite3.Error as erro:
 print("Houve um erro na remoção da informação solicitada , por favor repita a ação novamente")
finally #mensagem para sinalizar o fim da execução do programa.
 print(" Programa executado")

