import numpy as np
from math import sqrt
from Common import E

def Gauss(InputArray, vecC, R): # Non-iterative algoritm
    Alfa = 1 / (2*R**2)

    X = []
    Y = []

    h = []

    W = []

    for i in InputArray:
        X.append(i[0])
        Y.append(i[1])
    Y = np.array(Y, float)
    W = np.array(W, float)
    print(X)
    print(vecC)

    H = []
    for i in range(len(vecC)):
        for j in range(len(X)):
            h.append(E**(-Alfa*sqrt((X[j]-vecC[i])**2)**2))
        H.append(h.copy()) # Oni, syka, iz roditel'skogo massiva udalyautcha bez copirovania!! Piton govno
        h.clear()

    H = np.array(H, float)
    H = H.T
    print(H)
    HT = H.T

    W = np.dot(np.dot(np.linalg.inv(np.dot(HT, H)), HT), Y.T)
    print(W)


def main():
    InputArray = [[-2.0, -0.48], 
                  [-1.5, -0.78], 
                  [-1.0, -0.83], 
                  [-0.5, -0.67], 
                  [0.0, -0.20], 
                  [0.5, 0.70], 
                  [1.0, 1.48], 
                  [1.5, 1.17], 
                  [2.0, 0.20]]
    vecC = [-2.0, -1.0, 0.0, 1.0, 2.0] # Vector of centers
    Gauss(InputArray, vecC, 1.5)
main()
