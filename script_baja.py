import MySQLdb
import sys
import os
#pedimos el nombre
dominio = (sys.argv[1])
cortacadena=dominio.split(".")
nombre=cortacadena[0]
#abrimos una conexion
base = MySQLdb.connect(host="localhost", user="root", passwd="usuario", db="ftpd")
cursor=base.cursor()
#vemos si el usuario existe buscamos en mysql el nombre de usuario
consultausuario="select ndominio from usuarios where ndominio='%s';" %dominio
cursor.execute(consultausuario)
#consulta_usuario = cursor.fetchone()
if consultausuario == None:
        print "El usuario %s no existe"%nombre
        sys.exit
else:
        #borramos la carpeta personal
        os.system("rm -r /srv/www/%s" % nombre)
        #desabilitamos los virtualhost
        os.system("a2dissite %s>/dev/null"%dominio)
        #borramos los virtualhosts
        os.system("rm -r /etc/apache2/sites-available/%s"%dominio)
        #reiniciamos apache
        os.system("service apache2 restart>/dev/null")
        #borramos el usuario de mysql y las bases de datos
        borrarbases="drop database my%s"%nombre
        cursor.execute(borrarbases)
        base.commit()
        borrausuario=" drop user my%s@localhost" %nombre
        cursor.execute(borrausuario)
        base.commit()
        #borramos la columna de la tabla ftpd
        borracolumna="delete from usuarios where ndominio='%s';" %dominio
        cursor.execute(borracolumna)
        base.commit()
        base.close()
        #borramos el fichero db. donde 
        os.system("rm -r /var/cache/bind/db.%s" %dominio)
        #borramos la zona del fichero named.conf.local
        os.system("sed '/zone " + '"%s"'% dominio + "/,/};/d' /etc/bind/named.conf.local > temporal")
        os.system("mv temporal /etc/bind/named.conf.local")
        print "El usuario fue elimindado correctamente y ya no está en el hosting"

