import numpy as np
from Common import SingleJump

def Hopfield(X, W, Practice, T):
    W = np.array(W, int)
    X = np.array(X, int)
    Y0 = np.array(Practice[0], int)
    Y1 = []
    S = []
    W = np.dot(X.T, X)
    for i in range(len(W)):
        for j in range(len(W[0])):
            if(i == j):
                W[i][j] = 0
    print(W)
    print(Y0)
    tmp = 0
    for i in range(len(W)):      # 2.2
        for j in range(len(W[0])):
            tmp += W[i][j]*Y0[j]
        S.append(tmp)
        tmp = 0
    print(S)
    for j in range(len(Y0)):
        Y1.append(SingleJump(S[j], T))
    Y1 = np.array(Y1, int)
    print(Y1)
    print(np.sqrt(sum((Y1 - Y0)**2)))



def main():
    InputArray = [[1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 # NxM
                  [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1]] # 2 
    Practice =   [[1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 mod
                  [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1]] # 2 mod
    W = []
    Hopfield(InputArray, W, Practice, 0)
main()