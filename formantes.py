import parselmouth 
import statistics
from parselmouth import praat

# funcion para identificar los formates de un archivo de audio
def getFormantes(testfile):
    sound = parselmouth.Sound(testfile)

    f0min=75
    f0max=300
    pointProcess = praat.call(sound, "To PointProcess (periodic, cc)", f0min, f0max)

    formants = praat.call(sound, "To Formant (burg)", 0.0025, 5, 5000, 0.025, 50)

    numPoints = praat.call(pointProcess, "Get number of points")
    f1_list = []
    f2_list = []
    # f3_list = []
    for point in range(0, numPoints):
        point += 1
        t = praat.call(pointProcess, "Get time from index", point)
        f1 = praat.call(formants, "Get value at time", 1, t, 'Hertz', 'Linear')
        f2 = praat.call(formants, "Get value at time", 2, t, 'Hertz', 'Linear')
        # f3 = praat.call(formants, "Get value at time", 3, t, 'Hertz', 'Linear')
        f1_list.append(f1)
        f2_list.append(f2)
        # f3_list.append(f3)
    formante1, formante2 = 0,0
    if len(f1_list) != 0 and len(f2_list) != 0:
        formante1 = statistics.mean(f1_list)
        formante2 = statistics.mean(f2_list)
    # print(formante1)
    # print(formante2)
    formantes = [formante1, formante2]
    return formantes

# testfile = 'Audios/UH/UH_1.wav'
# form = getFormantes(testfile)
# print(form[0])
# print(form[1])
