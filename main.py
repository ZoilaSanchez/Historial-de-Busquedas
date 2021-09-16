import sqlite3
import getpass
import pymongo
import datetime
from tkinter import messagebox as MessageBox
###conexion a mongo

client = pymongo.MongoClient("mongodb+srv://m001-student:1234@cluster0.lo2p9.mongodb.net/library?retryWrites=true&w=majority")
print("Esta primera parte mostrará las bases de datos que esten incluyendo sus coleccions: ------------------")
collection = client.datos.historial

user=getpass.getuser() # obtener el usuario 
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
            """ if(y == "dia_visitado"):
                if(x[count] > yesterday):
                    print(x[count]) """
            count+=1
        if(json['dia_visitado'] > yesterday):
            collection.insert_one(json)

except con.OperationalError:   
    MessageBox.showwarning("Alerta", "Cerrar el navegador antes")

