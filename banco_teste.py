#!/usr/bin/env python3

import requests
import psycopg2
import cgi

form = cgi.FieldStorage()

nome = form.getvalue("nome")
matricula = form.getvalue("matricula")
curso = form.getvalue("curso")
disciplina = form.getvalue("disciplina_ingresso")
email = form.getvalue("email")
campus = form.getvalue("campus")
diretoria = form.getvalue("diretoria")
vinculo = form.getvalue("tipo_vinculo")
situacao = form.getvalue("situacao")
foto = form.getvalue("foto")

print ("Content-type: text/html\n\n")

print ("<HTML><HEAD>")

print("<meta charset =utf-8 />")
print("<title> Dados </title>")

print("<style type='text/css'>")
print('body{background-image: url("https://elemento79.com.br/wp-content/uploads/2013/12/seamless-gold-greek-key-background-pattern-vector-1195683.jpg")')
print('</style>')

strConexaoDefault  = "dbname=postgres user=postgres host=localhost password=123 "
strConexaoDBAlunos = "dbname= suap user=postgres host=localhost password=123 "
strSQLCriaDatabase = "CREATE DATABASE suap"
strSQLCriaTable    = "CREATE TABLE Dados_Suap (Nome VARCHAR(200) not null, Matricula BIGINT PRIMARY KEY, Curso VARCHAR(200) ,Disciplina varchar(200) ,Email VARCHAR(100),Campus varchar(200) ,Diretoria varchar (200) ,Vinculo varchar(50) ,Situacao varchar(50) ,Foto varchar(300));"
strSQLInsereDados = "INSERT INTO dados_suap VALUES ('{}',{},'{}','{}','{}','{}','{}','{}', '{}', '{}')".format(nome,matricula,curso,disciplina,email,campus,diretoria,vinculo,situacao,foto)


from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(strConexaoDefault)
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
try:
	cur.execute(strSQLCriaDatabase)
	conn.commit()
	conn.close()
	cur.close()
except psycopg2.Error as e:
	print(e)
	erro = 0

conn = psycopg2.connect(strConexaoDBAlunos)
cur = conn.cursor()

try:
		
	conn = psycopg2.connect(strConexaoDBAlunos)
	cur = conn.cursor()
	cur.execute(strSQLCriaTable)
	conn.commit()
	cur.close()
	conn.close()

except psycopg2.Error as e:
	print(e)
	erro = 1


try:
	conn = psycopg2.connect(strConexaoDBAlunos)
	cur = conn.cursor()
	cur.execute(strSQLInsereDados)
	conn.commit()
	conn.close()

except psycopg2.Error as e:
	print(e)

	erro = 2

if erro == 2:

	print('<h3 style="color:white;"> <center>')
	print(" Os dados ja existem no banco! ")
	print(" </center> </h3>")

else:	
 
	print('</HEAD> <BODY>')

	print('<h3 style="color:white;"> <center>') 
	print(" Dados salvos com sucesso!\n ")
	print(" Dados salvos no banco ")
	print(" </center> </h3>")
	
	print('</BODY></HTML>')
'''
# A intenção do código abaixo é listar os dados salvos no banco para o usuário

	strConexao = "dbname=suap user=postgres host=localhost"
	connConexao = psycopg2.connect(strConexao)
	curConexao = connConexao.cursor()

	curConexao.execute("select * from dados_suap")

	resultado = curConexao.fetchall()
	print(resultado)
	
	#for data in resultado:

		#if resultado['tipo_vinculo'] == 'Aluno':

		#	print ("Matricula: {0} Nome: {1} Email: {2} \n".format(data[0], data[1], data[2]))	


'''

