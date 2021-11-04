import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
titulo = []
cantidad=[]

f = open("C:/Users/zoili/Documents/GitHub/Historial-de-Busquedas/AnalisisConR/Filtrado_Tratamiento/AGraficar/enlacesmasbuscados.txt", "r")
for i, line in enumerate(f):
    if i % 2 != 0:
       titulo.append(line)
       #print(line)
    else:
      #  print(line)
        cantidad.append(int(line.strip()))


v = np.random.randint(0, 3, size=100)
plt.xlabel('Visitas')
plt.title('Páginas con visitas mayores a 100')

colors = plt.cm.jet(np.linspace(0,1,len(titulo)))
plt.barh(titulo, cantidad, color=colors[v])

for index, value in enumerate(cantidad):
    plt.text(value, index,
             str(value),color="blue")

plt.show()

