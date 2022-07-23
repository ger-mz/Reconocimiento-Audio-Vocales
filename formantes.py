import parselmouth 
import statistics
from parselmouth import praat

# funcion para identificar los formates de un archivo de audio
def getFormantes(testfile):
    # Cargando archivo de audio
    sound = parselmouth.Sound(testfile)

    f0min=75
    f0max=300
    pointProcess = praat.call(sound, "To PointProcess (periodic, cc)", f0min, f0max)

    formants = praat.call(sound, "To Formant (burg)", 0.0025, 5, 5000, 0.025, 50)

    numPoints = praat.call(pointProcess, "Get number of points")
    f1_list = []
    f2_list = []

    # leyendo formante 1 y 2 a lo largo del arhivo de audio
    for point in range(0, numPoints):
        point += 1
        t = praat.call(pointProcess, "Get time from index", point)
        f1 = praat.call(formants, "Get value at time", 1, t, 'Hertz', 'Linear')
        f2 = praat.call(formants, "Get value at time", 2, t, 'Hertz', 'Linear')
        
        f1_list.append(f1)
        f2_list.append(f2)
        
    formante1, formante2 = 0,0
    # Calculando promedio de las formantes
    if len(f1_list) != 0 and len(f2_list) != 0:
        formante1 = statistics.mean(f1_list)
        formante2 = statistics.mean(f2_list)
        
    formantes = [formante1, formante2]
    return formantes
