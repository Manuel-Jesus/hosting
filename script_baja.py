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
        
