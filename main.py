import tkinter 
from tkinter import Label, Button, ttk
from PIL import Image, ImageTk
# from tkinter import *
# from tkinter import ttk

# Bacdkground color 
bgcolor= '#800040'

def iniciar() :
    print("iniciar")


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

    # Boton de accion
    img = Image.open('img/microfono.png')
    img = img.resize((50, 50), Image.ANTIALIAS) 
    img = ImageTk.PhotoImage(img)
    botonGrabar = Button(interfaz, image=img, text="Grabar", compound="top", command=iniciar, bg='#480000', fg='#FFFFFF')
    botonGrabar.place(x = 200, y = 50)

    # Logos del politecnico
    ipn = Image.open('img/ipn.png')
    ipn = ipn.resize((120, 85), Image.ANTIALIAS) 
    ipn = ImageTk.PhotoImage(ipn)
    ipnLogo = Label(interfaz, image = ipn, bg='#FFFFFF', fg='#FFFFFF')
    # ipnLogo.config(bg='systemTransparent')
    ipnLogo.place(x = 0, y = 17)

    escom = Image.open('img/escom.png')
    escom = escom.resize((85, 85), Image.ANTIALIAS) 
    escom = ImageTk.PhotoImage(escom)
    escomLogo = Label(interfaz, image = escom, bg='#FFFFFF', fg='#FFFFFF')
    # ipnLogo.config(bg='systemTransparent')
    escomLogo.place(x = 370, y = 17)

    #Barra de progreso de la accion al accionar el boton
    pb = ttk.Progressbar(interfaz, orient="horizontal", length=200)
    pb.place(x = 140, y = 135)
    pb.config(mode="determinate", maximum=100, value = 0)
    pb.step(100)
    # pb.pack()

    label = Label(interfaz, text = 'Letra Encontrada:', font=("Verdana",12), bg='#480000', fg='#FFFFFF')
    label.place(x = 160, y = 175)
    # label.pack()

    interfaz.mainloop()

