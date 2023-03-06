from math import sqrt
from Common import *

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
            Fs = SigmoidLogistics(A, S)  # Activation function
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

def main():
    InputList = []
    minmax = []
    RandomFill(InputList, 10, -10, 10)
    UniqulizeMinMax(InputList, minmax)
    Normalize(InputList, minmax)
    SingleLayerPerceptron(len(InputList[0]) - 1, len(InputList), 1, 0.99, InputList, 50)
main()
