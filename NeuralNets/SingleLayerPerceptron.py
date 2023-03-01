from math import sqrt
from Common import *

E = 2.71828182845904523536

def UniqulizeMinMax(a, minmax):
    print("\nInput array length:", len(a), "\n")
    NumerizedPrint(a)
    b = []

    # First correction
    a.sort(key=lambda x: (x[0], x[1]))
    minmax.append([a[0][0], a[len(a) - 1][0]])
    print("\nSorted array(0, 1):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if (a[i][0] == a[i + 1][0] and a[i][1] == a[i + 1][1]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML data:", b)
    for i in reversed(range(len(b))):
        del (a[b[i]])
    b.clear()

    # Last correction
    a.sort(key=lambda x: (x[1], x[2]))
    minmax.append([a[0][1], a[len(a) - 1][1]])
    print("\nSorted array(1, 2):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if (a[i][1] == a[i + 1][1] and a[i][2] == a[i + 1][2]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML data:", b)
    for i in reversed(range(len(b))):
        del (a[b[i]])

    a.sort(key=lambda x: x[2])
    minmax.append([a[0][2], a[len(a) - 1][2]])
    a.sort(key=lambda x: x[3])
    minmax.append([a[0][3], a[len(a) - 1][3]])
    print("\nFinal array view:")
    NumerizedPrint(a)
    print("\nMin Max :", minmax)

def Normalize(array, minmax):
    for i in range(len(array)):
        for k in range(len(array[0]) - 1):
            array[i][k] = (array[i][k] - minmax[k][0]) / (minmax[k][1] - minmax[k][0])
        array[i][3] = (array[i][3] - minmax[3][0]) / (minmax[3][1] - minmax[3][0])

    print("\nNormalzed data: \n")
    NumerizedPrint(array)


def SingleLayerPerceptron(M, K, A, V, Input, Ages):  # M - inputs, K - outputs, A - feed parametr, V - learning speed, Input - input array 4*x, Ages - learning ages amount
    N = (M + 1)  # Weight coeff amount
    Nw = []
    Fs = 0.0
    for i in range(N):
        Nw.append(random.uniform(0, M ** -1))  # Weight coeff array
    Vd = V / (Ages + 1)  # Learning speed decrementation
    AgeLog = []  # Log of age
    delt = 0
    Err = []
    file = open("outputSLP.csv", "w")
    file.write("Neuron;Activation function;delta;w0;w1;w2;w3;\n\n")

    for counter in range(Ages):
        print("\nStart of age", counter, ":", "\n\nInput data(x1, x2, x3, y1): ")
        NumerizedPrint(Input)
        print("\nIterations(Neuron, Activation function, delta, Weight coefficients):")

        for i in range(0, K, 1):
            S = Nw[0] + (Nw[1] * Input[i][0] + Nw[2] * Input[i][1] + Nw[3] * Input[i][2])  # Neuron state
            Fs = 1 / (E **(-A*S) + 1)  # Activation function
            delt = Input[i][3] - Fs  # Error
            for j in range(0, N, 1):
                Nw[j] = Nw[j] + V * delt * Input[i][j]  # Error fixing
            AgeLog.append([S, Fs, delt, [Nw[0], Nw[1], Nw[2], Nw[3]]])
            file.write(str(S) + ";" + str(Fs) + ";" + str(delt) + ";" + str(Nw[0]) + ";" + str(Nw[1]) + ";" + str(Nw[2]) + ";" + str(Nw[3]) + "\n")
            tmp = 0
        for k in range(0, len(AgeLog), 1):
            tmp += AgeLog[i][2]**2
        Err.append(sqrt(tmp/K))
        NumerizedPrint(AgeLog)
        random.shuffle(Input)
        AgeLog.clear()       
        V -= Vd
        print("\nEnd of age\nError:", Err[counter], "\nNew learn speed:", V, "\n\n") 
        file.write("\n") 

    file.write("\n\n") 
    for i in range(len(Err)):
        file.write(str(i) + ";" + str(Err[i]) + "\n")    
    file.close()

    # Main() example:

    # from SingleLayerPerceptron import *
    # InputList = []
    # minmax = []
    # RandomFill(InputList, 10, -10, 10)
    # UniqulizeMinMax(InputList, minmax)
    # Normalize(InputList, minmax)
    # SingleLayerPerceptron(len(InputList[0]) - 1, len(InputList), 1, 0.99, InputList, 50)
