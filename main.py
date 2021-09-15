import sqlite3
import getpass

user=getpass.getuser() # obtener el usuario 
url='C:\\Users\\'+user+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History' # url para obtener el historial
con = sqlite3.connect(url)
cursor = con.cursor()
cursor.execute("SELECT url FROM urls")
urls = cursor.fetchall()
print(urls,"\n")
