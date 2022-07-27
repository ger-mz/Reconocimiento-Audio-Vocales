import librosa.display
import numpy as np
from matplotlib import pyplot as plt

def graficaAudio(muestras, tasa):
    plt.figure()
    librosa.display.waveshow(y=muestras, sr=tasa)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.title("Amplitud de Audio")
    plt.show()

def graficaEspectroFrecuencias(amplitudes, tasa):
    n = len(amplitudes)
    T = 1/tasa
    xf = np.linspace(0.0, 1.0/(2.0*T), n)
    fig, ax = plt.subplots()
    ax.plot(xf, amplitudes)
    plt.grid()
    plt.xlabel("Frecuencia")
    plt.ylabel("Magnitud")
    plt.title("Espectros de Frecuencias")
    plt.show()