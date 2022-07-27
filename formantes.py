import parselmouth 
import statistics
from parselmouth import praat
from scipy.spatial import distance
from numpy import isnan

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

def identificar(formante, promedios):
    a = (formante[0], formante[1])
    if formante[0] == 0 and formante[1] == 0:
        return ' '
    ans = ''
    aux = 1000000
    for val in promedios:
        for punto in promedios[val]:
            distancia = distance.euclidean(a, punto)
            print("val: ",val,"punto: ", punto," distancia: ", distancia)
            if distancia < aux:
                if val == 'AH':
                    ans = 'A'
                elif val == 'EH':
                    ans = 'E'
                elif val == 'IH':
                    ans = 'I'
                elif val == 'OH':
                    ans = 'O'
                elif val == 'UH':
                    ans = 'U'
                aux = distancia
    return ans

# Preprocesado de los audios pre grabados
def preProcesado():
    carpetas = ['AH','EH','IH','OH','UH']
    promedios1 = {'AH':[], 'EH':[], 'IH':[],'OH':[], 'UH':[]}
    for carpeta in carpetas:
        formantesComp = []
        for i in range(1,6,1):
            path = 'audio/'+carpeta+'/'+carpeta+'_'+str(i)+'.wav'
            aux = getFormantes(path)
            if isnan(aux[0]) or isnan(aux[1]):
                print('carpeta: '+carpeta+' range: '+str(i))
                print("aux: " + str(aux[0]))
                print("is nan")
                aux[0]=0
                aux[1]=0
            formantesComp.append((aux[0], aux[1]))
        promedios1[carpeta] = formantesComp
    print("Promedios: ")
    print(promedios1)
    print('')
    return promedios1