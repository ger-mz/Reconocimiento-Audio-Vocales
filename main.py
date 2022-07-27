from graficador import graficaAudio, graficaEspectroFrecuencias
from formantes import getFormantes, identificar, preProcesado
from tkinter import Tk, StringVar, Label, Button, ttk
from analisis import getAmplitudes, analizaAudio
from PIL import Image, ImageTk
from threading import Thread
from grabadora import grabar
from time import sleep

# Variables globales
global pb
global interfaz

# Bacdkground color 
bgcolor = '#800040'

# funcion para identificar la vocal en una grabacion usando formantes
def identificador() :
    grabar()
    promediosH = preProcesado()
    formante = getFormantes("audio/audio.wav")
    print("F1: ", formante[0])
    print("F2: ", formante[1])
    vocal = str(identificar(formante, promediosH)) 
    print("Vocal: "+vocal) 
    resultado = StringVar()
    vocalEncontrada = Label(interfaz, textvariable = resultado, font=("Verdana",70), bg=bgcolor, fg='#FFFFFF')
    vocalEncontrada.place(x = 195, y = 200)

    resultado.set('\t')
    resultado.set(vocal)

    # Funciones de analisis de audio
    analisis = analizaAudio("audio/audio.wav")
    amp = getAmplitudes(analisis['muestras'])

    # Botones de graficas
    b1 = Button(interfaz,bg='#480000', fg='#FFFFFF',cursor="hand1",text="Grafica de Audio",command=lambda: graficaAudio(analisis['muestras'], analisis['tasa_muestreo']))
    b1.place(x = 180, y = 370)
    b2 = Button(interfaz,bg='#480000', fg='#FFFFFF',cursor="hand1",text="Grafica de Espectro de Frecuencia",command=lambda: graficaEspectroFrecuencias(amp, int(analisis['tasa_muestreo'])))
    b2.place(x = 135, y = 405)


# accion de la barra de progreso
def barraProgreso() :
    pb.start(2)
    sleep(1.0)
    pb.stop()

def iniciar() :
    t1 = Thread(name = "barraProgreso", target = barraProgreso)
    t2 = Thread(name = "identificador", target = identificador)
    t1.start()
    t2.start()

if __name__ == "__main__" :
    # Iniciando la interfaz
    interfaz = Tk()
    # Configuracion de la ventana
    interfaz.geometry('480x470') 
    interfaz.config(bd = 10, bg = bgcolor)
    interfaz.title('Proyecto Vocales')
    # Informacion
    info = Label(interfaz,bd = 0, text = '          TCyS', font=("Verdana",12), bg = bgcolor, fg='#FFFFFF')
    info.place(x = 150, y = 17)

    # Boton de accion
    img = Image.open('img/microfono.png')
    img = img.resize((50, 50), Image.Resampling.LANCZOS) 
    img = ImageTk.PhotoImage(img)
    botonGrabar = Button(interfaz, image=img, text="Grabar", compound="top", command=iniciar, bg='#480000', fg='#FFFFFF')
    botonGrabar.place(x = 200, y = 50)

    # Logos del politecnico
    ipn = Image.open('img/ipn.png')
    ipn = ipn.resize((120, 85), Image.Resampling.LANCZOS) 
    ipn = ImageTk.PhotoImage(ipn)
    ipnLogo = Label(interfaz, image = ipn, bg='#FFFFFF', fg='#FFFFFF')
    ipnLogo.place(x = 0, y = 17)

    escom = Image.open('img/escom.png')
    escom = escom.resize((85, 85), Image.Resampling.LANCZOS) 
    escom = ImageTk.PhotoImage(escom)
    escomLogo = Label(interfaz, image = escom, bg='#FFFFFF', fg='#FFFFFF')
    escomLogo.place(x = 370, y = 17)

    #Barra de progreso de la accion al accionar el boton
    pb = ttk.Progressbar(interfaz, orient="horizontal", length=200)
    pb.place(x = 140, y = 135)
    pb.config(mode="determinate", maximum=65, value = 0)
    pb.step(65)

    label = Label(interfaz, text = 'Letra Encontrada:', font=("Verdana",12), bg='#480000', fg='#FFFFFF')
    label.place(x = 160, y = 175)

    interfaz.mainloop()