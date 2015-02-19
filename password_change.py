
import MySQLdb
import sys
import sys
servicio = (sys.argv[1])
usuario = (sys.argv[2])
contrasenanueva = (sys.argv[3])
#A continuacion procedemos por si el servicio es mysql
if servicio == "mysql":
        base = MySQLdb.connect(host="localhost", user="root", passwd="usuario", db="mysql")
        cursor = base.cursor()
        #buscamos si existe el usuario
        consultausuario = "select user from user where user='my"+usuario+"';"
        cursor.execute(consultausuario)
        consulta_usuario = cursor.fetchone()
        #si el usuario coinciden procedemos a cambiarla
        if consulta_usuario[0] == 'my'+usuario:
        #contrasenna nueva
                cambio = "SET PASSWORD FOR my"+usuario+"@localhost = PASSWORD('"+contrasenanueva+"');"
                cursor.execute(cambio)
                base.commit()
                print "contrasenna actualizada correctamente"
        else:
                print "usuario incorrecto"
                sys.exit
elif servicio == "ftp":
        base3 = MySQLdb.connect(host="localhost", user="root", passwd="usuario", db="ftpd")
        cursor3 = base3.cursor()
        #buscamos si existe el usuario
        consultausuario = "select username from usuarios where username='"+usuario+"';"
        cursor3.execute(consultausuario)
        consulta_usuario = cursor3.fetchone()

        #si el usuario coinciden procedemos a cambiarla
        if consulta_usuario[0]== usuario:
                cambio = "update usuarios set password = PASSWORD('"+contrasenanueva+"')where username='"+usuario+"';"
                cursor3.execute(cambio)
                base3.commit()
                print "contrasenna actualizada correctamente"
        #si no existe o si se equivoca introduciendo los parametros aparece un error
	else:
                print "usuario incorrecto"
else:
        print "si introduce mysql como primer parametro cambiara la contrasenna de el usuario mysql ademas como segundo el usuario,tercer parametro la nueva contrasenna o puede introducir ftp para cambiar la de el usuario ftp y los parametros usuario,nueva"
