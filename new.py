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

index = ['enero', 'feb', 'mar',
         'abr', 'may', 'jun', 'jul', 'ags', 'sep','oct', 'nov', 'dic']



df = pd.DataFrame({titulo[0]: top[0],titulo[1]: top[1],titulo[2]: top[2],titulo[3]: top[3]
                   ,titulo[4]: top[4],titulo[5]: top[5],titulo[6]: top[6]
                   ,titulo[7]: top[7],titulo[8]: top[8],titulo[9]: top[9]
                   ,titulo[10]: top[10]}, index=index)

#fig, ax = plt.subplots(2, 2, sharey = True)
#axes = df.plot.bar(rot=2, subplots=True)
#axes[1].legend(loc=2)
#ax[0, 0].bar(index, top[0])
df = pd.DataFrame({'index':index,titulo[0]: top[0],titulo[1]: top[1],titulo[2]: top[2],titulo[3]: top[3]
                   ,titulo[4]: top[4],titulo[5]: top[5],titulo[6]: top[6]
                   ,titulo[7]: top[7],titulo[8]: top[8],titulo[9]: top[9]
                   ,titulo[10]: top[10]})
fig, ax = plt.subplots(sharey = True)
df.plot.bar(x = 'index', y = titulo[0], ax = ax, color = 'tab:orange')
df.plot.bar(x = 'index', y = titulo[1], ax = ax)
plt.show()
#plt.show()