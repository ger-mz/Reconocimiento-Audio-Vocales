import tkinter 
from tkinter import Label
from PIL import Image, ImageTk
# from tkinter import *
# from tkinter import ttk

# Bacdkground color 
bgcolor= '#800040'


if __name__ == "__main__" :
    # Iniciando la interfaz
    interfaz = tkinter.Tk()
    # Configuracion de la ventana
    interfaz.geometry('480x470') 
    interfaz.config(bd = 10, bg = bgcolor)
    interfaz.title('Proyecto Vocales')
    # Informacion
    info = Label(interfaz,bd = 0, text = 'Grupo: 3CV16, TCyS', font=("Verdana",12), bg = bgcolor, fg='#FFFFFF')
    info.place(x = 150, y = 17)

    
    interfaz.mainloop()

