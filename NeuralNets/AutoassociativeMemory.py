import numpy as np
from Common import SingleJump, NumerizedPrint

def transpose(array):
    transposed = list()
    for i in range(len(array[0])):
        row = list()
        for sublist in array:
            row.append(sublist[i])
        transposed.append(row)
    return transposed

def multiply(array0, array1):
    multiplied = []
    for k in range(len(array0)):
        stringsum = []
        for i in range(len(array1[0])):
            string = 0
            for j in range(len(array0[0])):
                string += array0[k][j]*array1[j][i]
            stringsum.append(string)
        multiplied.append(stringsum.copy())
    return multiplied


def Hopfield(X, Xprac):
    W1 = multiply(transpose(X), X)
    for i in range(len(W1)):
        for j in range(len(W1[0])):
            if(i == j):
                W1[i][j] = 0
    print(W1)
    W = np.array([], int)
    X = np.array(X, int) # 1.1
    W = np.dot(X.T, X) # 1.2
    for i in range(len(W)):
        for j in range(len(W[0])):
            if(i == j):
                W[i][j] = 0
    print("X:")
    NumerizedPrint(X)
    print("W:\n", W)
    for prac in range(len(Xprac)):
        Y = [Xprac[prac]] # 2.1
        print("Y0:\n", Y)                   
        n = 1.0
        counter = 0
        while(n > 0.0):
            print("\nIteration ", counter)
            temp = [] 
            S = []
            for i in range(len(W)):  # 2.2
                tmp = 0
                for j in range(len(W[0])):
                    tmp += W[i][j]*Y[counter][j]
                S.append(tmp)
            print("S:\n", S)
            Y = list(Y)
            temp = [] 
            for j in range(len(Y[0])): # 2.3
                temp.append(SingleJump(S[j], 0))
            Y.append(temp)
            Y = np.array(Y, int)
            print("Y1:\n", Y[counter+1])   
            n = sum((Y[counter] - Y[counter+1])**2) # 2.4
            print("n:", n)
            if(counter > 1 and sum((Y[counter] - Y[counter - 2])**2) == 0 and sum((Y[counter - 1] - Y[counter - 3])**2) == 0):
                print("This image not recognized:\n", Y[counter])  
                break
            counter += 1



def main():
    InputArray = [[1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 # NxM
                  [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1]] # 2 
    Practice =   [[1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 mod
                  [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1]] # 2 mod
    Hopfield(InputArray, Practice)
    print(NumerizedPrint(transpose(InputArray)))
    print(NumerizedPrint(multiply(transpose(InputArray), InputArray)))
main()