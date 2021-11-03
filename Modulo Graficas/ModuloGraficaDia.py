import pandas as pd
import matplotlib.pyplot as plt
titulo = []
top=[]
semana=[]

f = open("C:/Users/zoili/Documents/GitHub/Historial-de-Busquedas/AnalisisConR/RProject/AGraficar/graficaSemanas.txt", "r")
for i, line in enumerate(f):
    if i % 2 == 0:
       titulo.append(line)
    else:
        palabras = line.split(",")
        semana=[]
        for palabra in palabras:
                 if(palabra.strip()!=""):
                     semana.append(int(palabra.strip()))
        top.append(semana)

index = ['lun', 'mar', 'mie',
         'jue', 'vie', 'sab', 'dom']
df = pd.DataFrame({titulo[0]: top[0],titulo[1]: top[1],titulo[2]: top[2],titulo[3]: top[3]
                   ,titulo[4]: top[4],titulo[5]: top[5],titulo[6]: top[6]
                   ,titulo[7]: top[7],titulo[8]: top[8],titulo[9]: top[9]
              }, index=index)

axes = df.plot.bar(rot=0, subplots=True,layout=(5,2),title ="Paginas mas visitadas por Semana")
axes[0, 1].set_title("")
axes[1, 1].set_title("")
axes[2, 1].set_title("")
axes[3, 1].set_title("")
axes[4, 1].set_title("")
axes[0, 0].set_title("")
axes[1, 0].set_title("")
axes[2, 0].set_title("")
axes[3, 0].set_title("")
axes[4, 0].set_title("")
plt.show()