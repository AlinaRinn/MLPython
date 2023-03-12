import Common

def ART1(inputArray, Rcr, lamda, V):
    # region variables
    W = [] # neuron
    T = [] # neuron
    Y = []
    R = []
    X = inputArray[0]
    WWinnerIndex = "No match"
    # endregion variables

    # cluster init 1.0
    def init(X, W, T): 
        tmp0 = []
        tmp1 = []
        for i in range(len(X)):
            tmp0.append((lamda*X[i])/(lamda - 1 + sum(X))) # 1.2
            tmp1.append(X[i])
        W.append(tmp0.copy())
        T.append(tmp1.copy())
    
    def printInfo(): 
        print("W:")
        Common.NumerizedPrint(W)
        print("\nT:")
        Common.NumerizedPrint(T)
        print("\nY:")
        Common.NumerizedPrint(Y)
        print("\nR:")
        Common.NumerizedPrint(R)
        print("Match to cluster (WWinner):", WWinnerIndex)

    init(X, W, T)     
    print("Iter 0: init")
    printInfo()
    # cluster compare # 2.0
    for e in range(1, len(inputArray), 1): 
        X = inputArray[e] # 2.1
        print("\n\nIter", e, "\nX:", X)
        temp = 0
        for i in range(len(W)):
            for j in range(len(W[0])):
                temp += W[i][j]*X[j] 
            Y.append(temp)
            temp = 0

        # region if we have cluster that match # 3.0
        temp = 0
        for i in range(len(T)): # 3.1
            for j in range(len(T[0])):
                temp += T[i][j]*X[j] # For all, its OK
            R.append(temp/sum(X))
            temp = 0
        
        winner = False
        for i in range(len(R)): 
            if (R[i] >= Rcr): # 3.2
                WWinnerIndex = R.index(R[i])
                for j in range(len(W[0])):
                    W[WWinnerIndex][j] = (1 - V)*W[WWinnerIndex][j] + V*(lamda*X[j]) / (lamda - 1 + sum(X))
                    T[WWinnerIndex][j] = (1 - V)*T[WWinnerIndex][j] + V*X[j]
                winner = True

        if(winner == False):
            init(X, W, T)
            print("No winner, new cluster added")
        #endregion

        printInfo()
        Y.clear()
        R.clear()
        WWinnerIndex = "No match"

def main(): 
    inputArray = [[1, 0, 1, 0, 1, 0, 1, 0, 1], # 1
                  [0, 1, 0, 1, 0, 1, 0, 1, 0], # 2
                  [1, 0, 1, 0, 1, 0, 1, 0, 0], # 1 mod
                  [0, 1, 1, 1, 0, 1, 0, 1, 0], # 2 mod
                  [0, 1, 0, 1, 0, 1, 0, 1, 1], # 2 mod
                  [1, 1, 1, 0, 1, 0, 1, 0, 1], # 1 mod
                  [1, 0, 1, 0, 0, 1, 0, 1, 0]] # 12 mod
    ART1(inputArray, 0.7, 2, 0.6)
main()
