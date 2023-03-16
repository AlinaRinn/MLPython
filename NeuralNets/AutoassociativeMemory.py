import numpy as np
from Common import SingleJump

def Hopfield(X, Xprac):
    W = np.array([], int)
    X = np.array(X, int) # 1.1
    W = np.dot(X.T, X) # 1.2
    for i in range(len(W)):
        for j in range(len(W[0])):
            if(i == j):
                W[i][j] = 0
    print("W:\n", W)

    for prac in range(len(Xprac)):
        Y = [Xprac[prac]] # 2.1
        print("Y0:\n", Y)                   
        n = 1.0
        counter = 0
        while(n > 0.0):
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
            print("Y1 - Y0:\n", Y[counter] - Y[counter+1])
            n = sum((Y[counter] - Y[counter+1])**2) # 2.4
            print("n:\n", n)
            counter += 1



def main():
    InputArray = [[1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 # NxM
                  [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1]] # 2 
    Practice =   [[1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 mod
                  [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1]] # 2 mod
    Hopfield(InputArray, Practice)
main()