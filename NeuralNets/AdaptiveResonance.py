import Common

def ART1(inputArray, Rcr, lamda, V):
    def init(X, W, T): # cluster init
        tmp0 = []
        tmp1 = []
        for i in range(len(X)):
            tmp0.append((lamda*X[i])/(lamda - 1 + sum(X)))
            tmp1.append(X[i])
        W.append(tmp0.copy())
        T.append(tmp1.copy())
    
    W = []
    T = []
    Y = []
    R = []
    X = inputArray[0]        
    init(X, W, T)     

    for e in range(1, len(inputArray), 1): # compare
        X = inputArray[e]
        temp = 0
        for i in range(len(W)):
            for j in range(len(W[0])):
                temp += W[i][j]*X[j]
            Y.append(temp)
            temp = 0

        for i in Y: # if all clusters mismatch
            temp += i
        if(temp == 0.0):
            init(X, W, T)  
            continue
        for i, j in X, Y:
            Y.index(max(Y))

        Common.NumerizedPrint(W)
        print("\n")
        Common.NumerizedPrint(T)
        print("\n")
        Common.NumerizedPrint(Y)
        print("\n")


def main(): 
    inputArray = [[1, 0, 1, 0, 1, 0, 1, 0, 1], # 1
                  [0, 1, 0, 1, 0, 1, 0, 1, 0], # 2
                  [1, 0, 1, 0, 1, 0, 1, 0, 0], # 1 mod
                  [0, 1, 1, 1, 0, 1, 0, 1, 0]] # 2 mod

    ART1(inputArray, 0.7, 2, 0.6)
main()