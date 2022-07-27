from numpy import abs
from librosa import load
from scipy import fft

def analizaAudio(path):
    muestras, tasa_muestreo = load(path, sr=None, mono=True, offset=0.0, duration=None)
    info = dict()
    info['muestras'] = muestras
    info['tasa_muestreo'] = tasa_muestreo
    return info
  
def getAmplitudes(muestras):
    n = len(muestras)
    fft_var = fft.fft(muestras)
    amplitudes = 2.0/n * abs(fft_var[:n//2])
    return amplitudes