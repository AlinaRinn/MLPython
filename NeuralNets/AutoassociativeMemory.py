import numpy as np

def Hopfield(X, W, Practice):
    W = np.array(W, int)
    X = np.array(X, int)
    Y = np.array(Practice[0], int)

    W = np.dot(X.T, X)
    for i in range(len(W)):
        for j in range(len(W[0])):
            if(i == j):
                W[i][j] = 0
    print(W)



def main():
    InputArray = [[1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 # NxM
                  [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1]] # 2 
    Practice = [[1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 mod
                  [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1]] # 2 mod
    W = []
    Hopfield(InputArray, W, Practice)
main()