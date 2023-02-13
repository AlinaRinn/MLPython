import random
from math import sqrt

E = 2.71828182845904523536

def Taubin(x, y, z):
    return (x**2 + 9*y**2/4 + z**2 - 1)**3 - x**2*z**3 - 9*y**2*z**3/80

def RandomFill(a, b, c, d):
    for i in range(b):
        a.append([random.randint(c, d), random.randint(c, d), random.randint(c, d), 0])
        a[i][3] = Taubin(a[i][0], a[i][1], a[i][2])

def NumerizedPrint(a):
    for i in range(len(a)):
        print("%3d) %s" % (i, a[i]))

def UniqulizeMinMax(a, minmax):
    print("\nInput array length:", len(a), "\n")
    NumerizedPrint(a)   
    b = []

    # First correction
    a.sort(key = lambda x: (x[0], x[1]))
    minmax.append([a[0][0], a[len(a)-1][0]])
    print("\nSorted array(0, 1):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if(a[i][0] == a[i+1][0] and a[i][1] == a[i+1][1]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML data:", b)
    for i in reversed(range(len(b))):
        del(a[b[i]])
    b.clear()

    # Last correction
    a.sort(key = lambda x: (x[1], x[2]))
    minmax.append([a[0][1], a[len(a)-1][1]])
    print("\nSorted array(1, 2):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if(a[i][1] == a[i+1][1] and a[i][2] == a[i+1][2]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML data:", b)
    for i in reversed(range(len(b))):
        del(a[b[i]])

    a.sort(key = lambda x: x[2])
    minmax.append([a[0][2], a[len(a)-1][2]])
    a.sort(key = lambda x: x[3])
    minmax.append([a[0][3], a[len(a)-1][3]])
    print("\nFinal array view:")
    NumerizedPrint(a)
    print("\nMin Max :", minmax)

def Normalize(a, minmax):
    for i in range(len(a)):
        for k in range(len(a[0]) - 1):
            a[i][k] = (a[i][k] - minmax[k][0]) / (minmax[k][1] - minmax[k][0]) 
        a[i][3] = (a[i][3] - minmax[3][0]) / (minmax[3][1] - minmax[3][0])

    print("\nNormalzed data: \n")
    NumerizedPrint(a)

def SingleLayerPerceptron(M, K, A, V, Input, Ages): # M - входы, K - выходы, A - параметр насыщения, V - скорость обучения, Input - входной массив, Ages - кол-во эпох обучения    
    N = (M + 1) # Количество весовых коэффициентов
    Nw = [] 
    for i in range(N):
        Nw.append(random.uniform(0, M**-1)) # Массив коэффициентов 
    Vd = V / (Ages + 1) # Размер декрементирования скорости обучения
    AgeLog = [] # Лог эпохи
    locErr = [] # Локальная погрешность

    for counter in range(Ages):
        print("\nStart of age", counter, ":", "\n\nInput data: ")
        NumerizedPrint(Input)
        print("\nIterations:")
        for i in range(K):
            S = Nw[0] + (Nw[1]*Input[i][0] + Nw[2]*Input[i][1] + Nw[3]*Input[i][2]) # Состояние нейрона      
            Fs = 1 / (E**-A*S + 1) # Функция активации
            delta = Input[i][3] - Fs # Погрешность
            locErr.append(delta**2)
            for j in range(N - 1):
                Nw[j + 1] = Nw[j] + V*delta*Input[i][j] # Корректировка погрешности 
            AgeLog.append([S, Fs, delta, Nw])
            print(AgeLog[i], "    ", locErr[i])  
        Err = sqrt((1/N)*sum(locErr))
        random.shuffle(Input)
        V -= Vd  
        print("\nEnd of age\nNeuron condition(last):", S, "\nActivation function(last):", Fs, "\nError:", Err*100, "%\nWeight coefficients:", Nw, "\nNew learn speed:", V, "\n\n")


def main():
    InputList = []
    minmax = []
    RandomFill(InputList, 10, -10, 10)
    UniqulizeMinMax(InputList, minmax)
    Normalize(InputList, minmax)
    SingleLayerPerceptron(len(InputList[0]) - 1, len(InputList), 1, 0.9, InputList, 10)

main()