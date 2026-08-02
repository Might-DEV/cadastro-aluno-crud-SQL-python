Sistema de Cadastro de Alunos (CRUD)
Sistema de linha de comando desenvolvido em Python com banco de dados MySQL, aplicando os conceitos fundamentais de CRUD (Create, Read, Update, Delete).

Projeto criado como parte dos meus estudos em Análise e Desenvolvimento de Sistemas, com foco em back-end.

📋 Funcionalidades
✅ Cadastrar novo aluno
📄 Listar todos os alunos
✏️ Atualizar dados de um aluno
🗑️ Deletar aluno
🛠️ Tecnologias utilizadas

Python 3
MySQL
Biblioteca mysql-connector-python
⚙️ Como executar o projeto
Instale a biblioteca necessária:
pip install mysql-connector-python
Crie o banco de dados no MySQL:
CREATE DATABASE cadastro_alunos;

USE cadastro_alunos;

CREATE TABLE alunos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    curso VARCHAR(100)
);
Ajuste as credenciais de conexão no início do arquivo app.py (host, user, password, database).

Execute o programa:

python app.py
