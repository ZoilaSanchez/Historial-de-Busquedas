import pandas as pd
import matplotlib.pyplot as plt


titulo = []
ene = []
feb = []
mar = []
abr =[]
may = []
jun =[]
jul =[]
ags = []
sep = []
oct = []
nov = []
dic = []

contador=1

contadorm=1

f = open("C:/Users/zoili/Documents/GitHub/Historial-de-Busquedas/AnalisisConR/RProject/AGraficar/graficaMes.txt", "r")


for i, line in enumerate(f):
    
    if i % 2 == 0:
      # print('El número', i, 'es impar.')
       #print(line )
       titulo.append(line)
       
    else:
       #print('El número', i, 'es par.')
       palabras = line.split(",")
       ene.append(palabras[0])
       feb.append(palabras[1])
       mar.append(palabras[2])
       abr.append(palabras[3])
       may.append(palabras[4])
       jun.append(palabras[5])
       jul.append(palabras[6])
       ags.append(palabras[7])
       sep.append(palabras[8])
       oct.append(palabras[9])
       nov.append(palabras[10])
       dic.append(palabras[11])

          




df = pd.DataFrame(list(zip(titulo,ene,feb,mar,abr,may,jun,jul,ags,sep,oct,nov,dic)), columns = ['empres','ene','feb','mar','abr','may','jun','jul','ags','sep','oct','nov','dic'])


print(df)
#plt.show()
axes = df.plot.bar(rot=0, subplots=True)
axes[1].legend(loc=2)
plt.show()
