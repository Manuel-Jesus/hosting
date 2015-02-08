import sys
import MySQLdb


#pedimos el nombre y el dominio que se usara

#nombre = (sys.argv[1])
#dominio = (sys.argv[2])

nombre = raw_input("Introduce tu nombre de usuario: ")
dominio = raw_input("Introduce el nombre de dominio: ")


#siguiente paso: conectarnos a la bbdd

conexion = MySQLdb.connect(host = "localhost", user = "root", passwd = "usuario", db = "ftpd")
cursor = conexion.cursor()

#comprobacion de si el usuario existe

consulta_usuario = "select username from usuarios where username = '%s';" %nombre
cursor.execute(consulta_usuario)
consulta_usuario = cursor.fetchone()

if consulta_usuario != None:
	print "El nombre de usuario ya esta registrado"
	sys.exit
else:
	consulta_dominio = "select ndominio from usuarios where ndominio = '%s';" %dominio
	cursor.execute(consulta_dominio)
	consulta_dominio = cursor.fetchone()

	if consulta_dominio != None:
		print "El nombre de dominio ya esta registrado"
		sys.exit
	else:
		print "Todo correcto"




