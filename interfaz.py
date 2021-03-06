
from tkinter import Tk, Label, Button
class VentanaEjemplo:
    def __init__(self, master):
        self.master = master
        # Asigna un título a la ventana
        master.title('HISTORIAL DE CHROME')
        master.geometry('400x200') # anchura x altura
        #center(master)
        # Asigna un color de fondo a la ventana. Si se omite
        # esta línea el fondo será gris
        master.configure(bg = 'white')
        # evitar que se el usuario lo ajuste
        master.resizable(width=False, height=False)

        self.etiqueta = Label(master, text="")
        self.etiqueta.pack()


        self.etiqueta= Label(master,text="Bienvenido a HISTORIAL", fg = "blue")
        self.etiqueta.config(font=('Consolas',15)) #Cambiar tipo y tamaño de fuente
        #self.etiqueta.place(relx=0.5, rely=0.5)
        self.etiqueta.pack()



        self.botonSaludo = Button(master, text="Generar Graficas", command=self.saludar)
        self.botonSaludo.pack(padx=0, pady=30)


        self.botonCerrar = Button(master, text="Cerrar", command=master.quit)
        self.botonCerrar.pack()
    def saludar(self):
        print("¡Hey!")

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


#Configuraciones para la pantalla       
root = Tk()
miVentana = VentanaEjemplo(root)
root.mainloop()