import sqlite3
import getpass
from tkinter.constants import FALSE, TRUE
import pymongo
import datetime
import pymysql
import datetime
import regex as re
import demoji
demoji.download_codes()
from tkinter import messagebox as MessageBox
#conexión a la bd
connection = pymysql.connect(

    host='localhost', #ip
    user='root',
    password='1234',
    db='historialchrom'
)
###conexion a mongo

client = pymongo.MongoClient("mongodb+srv://m001-student:1234@cluster0.lo2p9.mongodb.net/library?retryWrites=true&w=majority")
print("Esta primera parte mostrará las bases de datos que esten incluyendo sus coleccions: ------------------")
collection = client.datos.historial

user=getpass.getuser() # obtener el usuario 
self = connection.cursor()
#insert para usuarios      
theinsert="insert into usuario(Nombre) values ('"+user+"')"
self.execute(theinsert)
connection.commit()
#consulta del id max de usuarios
theselect="select max(idUsuario) from usuario"
self.execute(theselect)
#guardar datos de la consulta
tuplausuario=self.fetchall()
#convertir tupla a lista
listausuario=list(tuplausuario[0])

url='C:\\Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History' # url para obtener el historial
con = sqlite3.connect(url)
cursor = con.cursor()
try:  
    elements = ["url", "titulo", "dia_visitado"]   
    cursor.execute("SELECT url, title, datetime(last_visit_time/1e6-11644473600,'unixepoch','localtime') FROM urls")
    urls = cursor.fetchall()
    print(urls,"\n")
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = str(yesterday) + " 00:00:00" #cada vez que se prenda la computadora subiremos a la bd los datos del historial del dia de ayer
    print(yesterday)
    for x in urls:
        json = {}
        count = 0
        for y in elements:
            json[y] = x[count]
            #print(x[count])
            #print(count)
            if (count==0):
                #insertar en busqueda
                theinsert2=f"insert into busqueda(Titulo,Usuario_idUsuario) values('{x[0]}',{listausuario[0]})"
                self.execute(theinsert2)
                connection.commit()
            elif(count==2):
                guardar= TRUE
                urlenlista=list(x[1])
                #print(urlenlista)
                for letra in urlenlista:
                    laurl="".join(urlenlista)
                    emojis = demoji.findall(laurl)
                    # Print converted emojis
                    #print(emojis)
                    #print("aqui que pex"+letra)
                    if (letra=="'"):
                        #print("encontro comilla simple")
                        letra='!'
                        guardar=FALSE
                    elif(emojis):
                        ##print(emojis)
                        guardar=FALSE
                       
                if (guardar==TRUE):
                   theinsert2=f"insert into Enlace(URL,diavicitado) values('{laurl}','{x[2]}')"
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
                """ if(y == "dia_visitado"):
                if(x[count] > yesterday):
                    print(x[count]) """
            count+=1
        if(json['dia_visitado'] > yesterday):
          #  collection.insert_one(json)
          print ("hooy")

except con.OperationalError:   
    MessageBox.showwarning("Alerta", "Cerrar el navegador antes")

