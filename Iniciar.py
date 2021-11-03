import tkinter
import pandas as pd
import subprocess
import matplotlib.pyplot as plt

root = tkinter.Tk()
root.title("Historial")
root.geometry("575x250")

frame_title = tkinter.Frame(root)
frame_fields = tkinter.Frame(root)
frame_fields1 = tkinter.Frame(root)
frame_scan = tkinter.Frame(root)
frame_scan1 = tkinter.Frame(root)
frame_fields2 = tkinter.Frame(root)


def Ver_Scrip():
    print("Verificar si se puede leer el script")
    subprocess.Popen("C:/Users/zoili/Documents/GitHub/Historial-de-Busquedas/AnalisisConR/Filtrado_Tratamiento/preuba.R", shell=True)
    stdout, stderr = proc.communicate() 
    pass
def Grafica_mes():
    print("generamos el mes")
    titulo = []
    top=[]
    meses=[]

    f = open("C:/Users/zoili/Documents/GitHub/Historial-de-Busquedas/AnalisisConR/Filtrado_Tratamiento/AGraficar/graficaMes.txt", "r")
   # C:\Users\zoili\Documents\GitHub\Historial-de-Busquedas\AnalisisConR\Filtrado_Tratamiento\AGraficar
    for i, line in enumerate(f):
        if i % 2 == 0:
           titulo.append(line)
        else:
            palabras = line.split(",")
            meses=[]
            for palabra in palabras:
                     if(palabra.strip()!=""):
                         meses.append(int(palabra.strip()))
            top.append(meses)

    index = ['ene', 'feb', 'mar',
             'abr', 'may', 'jun', 'jul', 'ags', 'sep','oct', 'nov', 'dic']
    df = pd.DataFrame({titulo[0]: top[0],titulo[1]: top[1],titulo[2]: top[2],titulo[3]: top[3]
                       ,titulo[4]: top[4],titulo[5]: top[5],titulo[6]: top[6]
                       ,titulo[7]: top[7],titulo[8]: top[8],titulo[9]: top[9]
                  }, index=index)

    axes = df.plot.bar(rot=0, subplots=True,layout=(5,2),title ="Paginas mas visitadas por mes")
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


    pass
def Grafica_dia():
    print("generamos el dia")
    titulo = []
    top=[]
    semana=[]

    f = open("C:/Users/zoili/Documents/GitHub/Historial-de-Busquedas/AnalisisConR/Filtrado_Tratamiento/AGraficar/graficaSemanas.txt", "r")
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
    pass
def top_10():
   print("generamos el top")
   pass

root.resizable(width=False, height=False)

title = tkinter.Label(root, text="Bienvenido a Historial", font=("Consolas", 24))
title.grid(pady=(0, 500),padx=(0, 300))

frame_fields.grid(row=0, column=0, padx=(0, 200), pady=(100, 0))
start_date_lbl = tkinter.Label(frame_fields, text="* Modulo de Datos", font=("Consolas", 16))
start_date_lbl.grid( padx=(20,50), pady=(0,500))


frame_fields2.grid(row=0, column=0, padx=(0, 0), pady=(0, 200))
scan_btn = tkinter.Button(frame_scan1, text="Generar", command=Ver_Scrip, height=1, width=8, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(0, 325),pady=(0,400))



frame_fields1.grid(row=0, column=1, padx=(0, 0), pady=(0, 200))

start_date_lbl1 = tkinter.Label(frame_fields, text="* Modulo de Graficas", font=("Consolas", 16))
start_date_lbl1.grid(column=1, row=0,padx=(0,150), pady=(0,500))

frame_scan1.grid(row=0, column=0, padx=(0, 280), pady=(100, 0))
scan_btn = tkinter.Button(frame_scan1, text="Mes", command=Grafica_mes, height=1, width=0, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(75, 0),pady=(0,400))

scan_btn = tkinter.Button(frame_scan1, text="Día", command=Grafica_dia, height=1, width=0, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(200, 0),pady=(0,400))

scan_btn = tkinter.Button(frame_scan1, text="Top 10", command=top_10, height=1, width=0, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(360, 0),pady=(0,400))

root.mainloop()
