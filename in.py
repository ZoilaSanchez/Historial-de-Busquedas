import tkinter

root = tkinter.Tk()
root.title("Historial")
root.geometry("575x250")

frame_title = tkinter.Frame(root)
frame_fields = tkinter.Frame(root)
frame_fields1 = tkinter.Frame(root)
frame_scan = tkinter.Frame(root)
frame_scan1 = tkinter.Frame(root)
frame_fields2 = tkinter.Frame(root)
#frame_credentials = tkinter.Frame(root)
#frame_site = tkinter.Frame(root)
#frame_change = tkinter.Frame(root)


def passx():
    print("hol")
    pass
def saludar():
    print("¡Hey!")
    pass
def Ver_Scrip():
   print("generamos el script")
   pass
def Grafica_mes():
   print("generamos el mes")
   pass
def Grafica_dia():
   print("generamos el dia")
   pass
def top_10():
   print("generamos el top")
   pass

root.resizable(width=False, height=False)
#frame_title.grid(row=0, column=0, padx=(50, 0),pady=(0, 0))
title = tkinter.Label(root, text="Bienvenido a Historial", font=("Consolas", 24))
title.grid(pady=(0, 500),padx=(0, 300))

frame_fields.grid(row=0, column=0, padx=(0, 200), pady=(100, 0))
start_date_lbl = tkinter.Label(frame_fields, text="* Modulo de Datos", font=("Consolas", 16))
start_date_lbl.grid( padx=(20,50), pady=(0,500))


#start_date_unp = tkinter.Entry(frame_fields, width=11, font=("Consolas", 16))
#start_date_unp.grid(column=1, row=0)
#start_date = start_date_unp.get()


#end_date_lbl = tkinter.Label(frame_fields, text="Enter the end date: ", font=("Consolas", 16))#end_date_lbl.grid(column=0, row=1)

#end_date_unp = tkinter.Entry(frame_fields, width=11, font=("Consolas", 16))
#end_date_unp.grid(column=1, row=1)
#end_date = end_date_unp.get()

frame_fields2.grid(row=0, column=0, padx=(0, 0), pady=(0, 200))
scan_btn = tkinter.Button(frame_scan1, text="Generar", command=saludar, height=1, width=8, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(0, 325),pady=(0,400))
#frame_credentials.grid(row=2, column=0)


frame_fields1.grid(row=0, column=1, padx=(0, 0), pady=(0, 200))

start_date_lbl1 = tkinter.Label(frame_fields, text="* Modulo de Graficas", font=("Consolas", 16))
start_date_lbl1.grid(column=1, row=0,padx=(0,150), pady=(0,500))

#frame_scan.grid(row=0, column=0, padx=(0, 100), pady=(100, 0))
frame_scan1.grid(row=0, column=0, padx=(0, 280), pady=(100, 0))
scan_btn = tkinter.Button(frame_scan1, text="Mes", command=passx, height=1, width=0, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(75, 0),pady=(0,400))

scan_btn = tkinter.Button(frame_scan1, text="Día", command=passx, height=1, width=0, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(200, 0),pady=(0,400))

scan_btn = tkinter.Button(frame_scan1, text="Top 10", command=passx, height=1, width=0, font=("Consolas", 16))
scan_btn.grid(row=0, column=1, padx=(360, 0),pady=(0,400))

#credential = tkinter.IntVar(value=0)
#tkinter.Radiobutton(frame_credentials, text="Username", variable=credential, value=1, font=("Consolas", 16)).grid(column=1, row=4, sticky="W", pady=(43, 50))
#tkinter.Radiobutton(frame_credentials, text="Password", variable=credential, value=2, font=("Consolas", 16)).grid(column=1, row=5, sticky="W")
#frame_site.grid(row=2, column=1, pady=(40, 0))
#site = tkinter.IntVar(value=0)
#tkinter.Radiobutton(frame_site, text="PearsonVUE", variable=site, value=1, font=("Consolas", 16)).grid(column=0, row=0, sticky="W", pady=8)
#tkinter.Radiobutton(frame_site, text="Kryterion", variable=site, value=2, font=("Consolas", 16)).grid(column=0, row=1, sticky="W")
#tkinter.Radiobutton(frame_site, text="PSI PAN", variable=site, value=3, font=("Consolas", 16)).grid(column=0, row=2, sticky="W", pady=8)
#tkinter.Radiobutton(frame_site, text="Scantron", variable=site, value=4, font=("Consolas", 16)).grid(column=0, row=3, sticky="W")
#tkinter.Radiobutton(frame_site, text="PSI Atlas", variable=site, value=5, font=("Consolas", 16)).grid(column=0, row=4, sticky="W", pady=8)
#frame_change.grid(row=2, column=2, padx=25, pady=(20, 0))
#change_btn = tkinter.Button(frame_change, text="Change", command=passx, height=2, width=8, font=("Consolas", 16))
#change_btn.grid(column=3, row=3)
root.mainloop()
 