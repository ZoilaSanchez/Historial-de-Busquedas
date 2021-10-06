import sqlite3
import getpass
import pymongo
import datetime
import pymysql
import datetime
from tkinter import messagebox as MessageBox
import certifi
#conexión a la bd
connection = pymysql.connect(

    host='bellouzr9e3zw1qlid1v-mysql.services.clever-cloud.com', #ip
    user='upyun9kofbkvbewp',
    password='8Vc5VVsqs1PFuxB2irAy',#'PfMkT'YACM9$Jn
    db='bellouzr9e3zw1qlid1v'
)
###conexion a mongo
user=getpass.getuser() # obtener el usuario 
url='C:\\Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History' # url para obtener el historial
con = sqlite3.connect(url)
cursor = con.cursor()

try:  
    client = pymongo.MongoClient("mongodb+srv://m001-student:1234@cluster0.lo2p9.mongodb.net/library?retryWrites=true&w=majority", tlsCAFile=certifi.where())
    print("Esta primera parte mostrará las bases de datos que esten incluyendo sus coleccions: ------------------")
    collection = client.datos.historial

    self = connection.cursor()
    #Extraer el usuario       
    theselect="SELECT w.nombre AS Nombre FROM  usuario w WHERE w.Nombre=('"+user+"')"
    self.execute(theselect)
    #guardar datos de la consulta
    nombre_usuario=self.fetchone()# obtener un dato

    if(nombre_usuario==None):     
        theinsert="insert into usuario(Nombre) values ('"+user+"')"
        self.execute(theinsert)
        connection.commit() 

    theselect="SELECT w.idUsuario AS id FROM  usuario w WHERE w.Nombre=('"+user+"')"
    self.execute(theselect) 
    #guardar datos de la consulta
    id_usu=self.fetchone()[0] # obtener el dato del id
    elements = ["url", "titulo", "dia_visitado"]   
    cursor.execute("SELECT url, title, datetime(last_visit_time/1000000-11644473600,'unixepoch','localtime') FROM urls")
    urls = cursor.fetchall()
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday = str(yesterday) + " 00:00:00" #cada vez que se prenda la computadora subiremos a la bd los datos del historial del dia de ayer
    print(yesterday)
    for x in urls:
        json = {}
        count = 0
        for y in elements:
            json[y] = x[count]
            """ if(y == "dia_visitado"):
                if(x[count] > yesterday):
                    print(x[count]) """
            count+=1
        if(json['dia_visitado'] > yesterday):
           collection.insert_one(json)
    # insertar en bd Relacional
    for x in urls:
            count = 0
        #for y in elements:
        #print(x[count] , yesterday )
            if(x[count+2]>yesterday):
                print("Fecha a evaluar es:" , yesterday ,x[count+2] )
                
                #print(x[count+2] )
                titulo=x[count+1].replace("'","")
                print(x[count])
                url=x[count].replace("'","")
                if(titulo!=""):
                    print(titulo)
                    theinsert2=f"insert into busqueda(Titulo,Usuario_idUsuario) values('{titulo}',{id_usu})"
                    self.execute(theinsert2)
                    connection.commit()
                    theinsert2=f"insert into Enlace(URL,diavicitado) values('{url}','{x[count+2]}')"
                    self.execute(theinsert2)
                    connection.commit()
                    #Consulta del id max de enlace
                    theselect3="select max(idEnlaces) from Enlace"
                    self.execute(theselect3)
                    idenlace=self.fetchone()[0]
                    print(idenlace)
                    theinsert2=f"insert into Usuario_has_Enlace(Enlace_idEnlaces,Usuario_idUsuario) values({idenlace},{id_usu})"
                    self.execute(theinsert2)
                    connection.commit()
            count+=1
except con.OperationalError:   
    MessageBox.showwarning("Alerta", "Cerrar el navegador antes")

