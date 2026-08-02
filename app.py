import mysql.connector
conexao= mysql.connector.connect(
host= "localhost",
user="root",
password = "",
database= "cadastro_alunos"
)
cursor=conexao.cursor()

def cadastrar_aluno():
  nome =input("Nome do aluno...")
  email=input("Email do aluno...")
  curso =input("Curso do aluno...")
  cursor.execute("INSERT INTO alunos (nome,email,curso) VALUES (%s,%s,%s)", (nome,email,curso))
  conexao.commit()
  print("Aluno cadastrado com sucesso!\n")

def listar_aluno():
  cursor.execute("SELECT * FROM alunos")
  alunos=cursor.fetchall()
  for aluno in alunos:
    print(aluno)
    print()

def atualizar_aluno():
  id_aluno =input("Digite o ID do aluno que deseja atualizar: ")
  novo_curso= input("Digite o novo curso:  ")
  cursor.execute("UPDATE alunos SET curso = %s WHERE id = %s",(novo_curso,id_aluno))
  conexao.commit()
  print("Aluno atualizado com sucesso!\n")

def deletar_aluno():
  id_aluno =input("Digite o ID do aluno que deseja deletar: ")
  cursor.execute("DELETE FROM alunos WHERE id = %s ",(id_aluno,))
  conexao.commit()
  print("Aluno deletado com sucesso!\n")


while True:
  print("==== SISTEMA DE CADASTRO DE ALUNOS ====")
  print( "1 - Cadastrar aluno")
  print("2 - Listar  alunos")
  print("3 - Atualizar aluno")
  print("4 -  Deletar aluno")
  print("0 - Sair")

  opcao =input("Escolha uma opção: ")

  if opcao == "1":
    cadastrar_aluno()
  elif opcao == "2":
    listar_aluno()
  elif opcao == "3":
    atualizar_aluno()
  elif opcao == "4":
    deletar_aluno()
  elif opcao == "0":
    print("Encerrando o sistema...")
    break
  else:
      print("Opcão inválida,tente novamente.\n")  
