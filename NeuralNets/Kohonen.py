from math import sqrt
import Common

def Kohonen(InputArray, W, V, claster, Eras): # Self-learning
    Vdecrement = V/Eras
    R = []
    Rtmparray = []
    Rtmp = 0
    WWinnerIndex = 0

    for e in range(Eras):
        print(V, Vdecrement)
        for j in range(claster):
            for i in range(len(InputArray[0])):
                Rtmp += (InputArray[j][i]-W[j][i])**2
            Rtmp = sqrt(Rtmp)
            Rtmparray.append(Rtmp)
            Rtmp = 0
        WWinnerIndex = Rtmparray.index(min(Rtmparray))
        print("Winner index: ", WWinnerIndex)
        for i in range(len(W[0])):
            W[WWinnerIndex][i] = W[WWinnerIndex][i] + V*(InputArray[WWinnerIndex][i] - W[WWinnerIndex][i])
        R.append(Rtmparray.copy())
        Rtmparray.clear()        
        V -= Vdecrement
    print(R, W)


def main():
    InputArray = [[1.00, 1.00, 0.17, 0.78, 0.70, 0.77, 0.68], # x1
                  [1.00, 0.00, 0.17, 0.58, 0.35, 0.00, 0.00], # x2
                  [0.00, 0.00, 0.17, 0.58, 0.35, 0.70, 0.60], # xM
                  [1.00, 1.00, 1.00, 0.77, 0.84, 0.75, 1.00], # 
                  [0.00, 1.00, 0.33, 0.77, 0.70, 0.71, 0.71],
                  [0.00, 1.00, 0.17, 0.77, 0.90, 0.87, 0.63],
                  [0.00, 1.00, 0.00, 0.78, 0.65, 0.74, 0.81],
                  [1.00, 0.00, 0.00, 0.52, 0.58, 0.59, 0.63],
                  [1.00, 0.00, 0.00, 0.57, 0.24, 0.68, 0.49],
                  [1.00, 0.00, 0.17, 0.52, 0.35, 0.13, 0.00],
                  [0.00, 1.00, 1.00, 0.90, 0.99, 1.00, 1.00],
                  [0.00, 1.00, 0.17, 0.89, 0.88, 0.70, 0.63],
                  [1.00, 0.00, 0.00, 0.61, 0.00, 0.05, 0.49],
                  [0.00, 1.00, 0.83, 0.83, 0.72, 0.77, 0.81],
                  [1.00, 0.00, 0.00, 0.00, 0.03, 0.03, 0.49],
                  [0.00, 1.00, 0.17, 0.65, 0.66, 0.68, 0.49],
                  [1.00, 1.00, 0.67, 1.00, 1.00, 0.89, 1.00],
                  [0.00, 1.00, 1.00, 0.85, 0.94, 0.92, 0.81],
                  [1.00, 1.00, 0.83, 0.52, 0.58, 0.74, 0.49],
                  [1.00, 0.00, 0.00, 0.57, 0.35, 0.03, 0.63]]
    Common.NumerizedPrint(InputArray)
    
    W = [[0.20, 0.20, 0.30, 0.40, 0.40, 0.20, 0.50], # claster 1    
         [0.20, 0.80, 0.70, 0.80, 0.70, 0.70, 0.80], # claster 2
         [0.80, 0.20, 0.50, 0.50, 0.40, 0.40, 0.40], # claster 3
         [0.80, 0.80, 0.60, 0.70, 0.70, 0.60, 0.70]] # claster 4
    Common.NumerizedPrint(W)
    Kohonen(InputArray, W, 0.3, 4, 1)

main()
