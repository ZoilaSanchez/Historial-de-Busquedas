import pymongo
import regex as re
import getpass
import plotly.express as px
import pandas as pd
user=getpass.getuser() # obtener el usuario 
url='C:\\Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History' # url para obtener el historial
client = pymongo.MongoClient("mongodb+srv://m001-student:1234@cluster0.lo2p9.mongodb.net/library?retryWrites=true&w=majority")
collection = client.datos.historial
datos = []
for x in client.datos.historial.find(): 
    datos.append(x)
    print(x)
print(len(datos))
contadorFacebook = 0
contadorLandivar = 0
contadorYoutube = 0
contadorGoogle = 0
contador = 0
for x in datos:
    contador +=1
    if re.search('^https://www.facebook', x["url"]):
        print(x)
        contadorFacebook+=1
    elif(re.search('^https://www.url', x["url"])):
        print(x)
        contadorLandivar+=1
    elif(re.search('^https://www.youtube', x["url"])):
        print(x)
        contadorYoutube+=1
    elif(re.search('^https://www.google', x["url"])):
        print(x)
        contadorGoogle+=1
print("La cantidad de veces visitado Facebook es ",contadorFacebook)
print("La cantidad de veces visitado la página de la universidad es ",contadorLandivar)
print("La cantidad de veces visitado la página de Youtube es ",contadorYoutube)
print("La cantidad de veces visitado la página de Youtube es ",contadorGoogle)
random_x = [contadorFacebook, contadorLandivar, contadorYoutube, contadorGoogle]
names = ['Facebook', 'Landivar', 'Youtube', 'Google'] 
fig = px.pie(values=random_x, names=names)
fig.show()
df1 = pd.DataFrame(dict(time=['Total', 'Google']))
df2 = pd.DataFrame(dict(market=[contador, contadorGoogle]))
fig = px.bar(df1, x=df1.time, y=df2.market)
fig.show()