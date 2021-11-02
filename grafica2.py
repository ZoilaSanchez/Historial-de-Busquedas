
import pandas as pd
import matplotlib.pyplot as plt

titulo = []
top=[]
meses=[]

f = open("C:/Users/zoili/Documents/GitHub/Historial-de-Busquedas/AnalisisConR/RProject/AGraficar/graficaMes.txt", "r")


for i, line in enumerate(f):

    if i % 2 == 0:
      # print('El número', i, 'es impar.')
       #print(line )
       titulo.append(line)

    else:
        palabras = line.split(",")
        meses=[]
        for palabra in palabras:
                 if(palabra.strip()!=""):
                     meses.append(int(palabra.strip()))
        top.append(meses)

print(titulo)
print(top)
print(top[0])

index = ['ene', 'feb', 'mar',
         'abr', 'may', 'jun', 'jul', 'ags', 'sep','oct', 'nov', 'dic']



df = pd.DataFrame({titulo[0]: top[0],titulo[1]: top[1],titulo[2]: top[2],titulo[3]: top[3]
                   ,titulo[4]: top[4],titulo[5]: top[5],titulo[6]: top[6]
                   ,titulo[7]: top[7],titulo[8]: top[8],titulo[9]: top[9]
                ,titulo[10]: top[10]}, index=index)


ax = df.plot.bar(rot=0)
plt.show()





df = pd.DataFrame({titulo[0]: top[0],titulo[1]: top[1],titulo[2]: top[2],titulo[3]: top[3]
                   ,titulo[4]: top[4],titulo[5]: top[5],titulo[6]: top[6]
                   ,titulo[7]: top[7],titulo[8]: top[8],titulo[9]: top[9]
              }, index=index)

axes = df.plot.bar(rot=0, subplots=True,layout=(5,2),title ="Paginas mas visitadas por mes")
#axes[0,1].legend(loc=3)
axes[0, 1].set_title("")
axes[1, 1].set_title("")
axes[2, 1].set_title("")
axes[3, 1].set_title("")
axes[4, 1].set_title("")
#axes[5, 1].set_title("")
axes[0, 0].set_title("")
axes[1, 0].set_title("")
axes[2, 0].set_title("")
axes[3, 0].set_title("")
axes[4, 0].set_title("")
#axes[5, 0].set_title("")

plt.show()
