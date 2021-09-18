import pymysql
import datetime

laprueba="prueba1"
titulo="titulo1"
busqueda="busqueda1"
val=1
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday = str(yesterday) + " 00:00:00" #cada vez que se prenda la computadora subiremos a la bd los datos del historial del dia de ayer
print(yesterday)

#conexión a la bd
connection = pymysql.connect(

    host='localhost', #ip
    user='root',
    password='1234',
    db='historialchrom'
)


self = connection.cursor()
#insert para usuarios      
theinsert="insert into usuario(Nombre) values ('"+laprueba+"')"
self.execute(theinsert)
connection.commit()

#consulta del id max de usuarios
theselect="select max(idUsuario) from usuario"
self.execute(theselect)
#guardar datos de la consulta
tuplausuario=self.fetchall()
#convertir tupla a lista
listausuario=list(tuplausuario[0])
#insertar en busqueda
theinsert2=f"insert into busqueda(Titulo,Usuario_idUsuario) values('{titulo}',{listausuario[0]})"
self.execute(theinsert2)
connection.commit()

theinsert2=f"insert into Enlace(URL,diavicitado) values('{titulo}','{yesterday}')"
self.execute(theinsert2)
connection.commit()
#Consulta del id max de enlace
theselect3="select max(idEnlaces) from Enlace"
self.execute(theselect3)
#guardar datos de la consulta
tuplaenlace=self.fetchall()
#convertir tupla a lista
listaenlace=list(tuplaenlace[0])
theinsert2=f"insert into Usuario_has_Enlace(Enlace_idEnlaces,Usuario_idUsuario) values({listaenlace[0]},{listausuario[0]})"
self.execute(theinsert2)
connection.commit()

