import Common

def Cosco(X, Y, X0):
    W = list(Common.multiply(Common.transpose(X), Y))
    Common.NumerizedPrint(W)

    for e in range(len(X0)):
        S1 = list(Common.multiply(Common.transpose(W), Common.transpose([X0[e]])))
        Common.NumerizedPrint(S1)
        S2 = list()
        Y1 = list()
        X1 = list()
        counter = 0
        while True:
            print("Iteration ", counter)
            Yprev = Y1.copy()
            Y1.clear()
            for i in range(len(S1)):
                for j in range(len(S1[0])):
                    Y1.append([Common.SingleJump(S1[i][j], 0)])
            print(Y1)

            S2 = Common.multiply(W, Y1)
            print(S2)
            for i in range(len(S2)):
                for j in range(len(S2[0])):
                    X1.append([Common.SingleJump(S2[i][j], 0)])
            print(X1)
            if (counter > 0):
                n = sum(Common.powList(Common.difference2dim(Y1, Yprev)))
                if (n == 0):
                    switcher = False
                    print("n = 0, this means that outputs are stabilized")
                    for i in range(len(Y)):  # 2.2
                        if (Y[i] == Common.dim2to1(Y1)):
                            print("Match to training image", i)
                            switcher = True
                    if (switcher == False):
                        print("No Matches to training images")
                    break

            S1 = Common.multiply(Common.transpose(W), X1)
            Common.NumerizedPrint(S1)
            counter += 1
            X1.clear()

def main(): 
    inputArray = [[1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 1, -1, 1, -1, -1, 1],
                  [1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, 1, 1, 1]]
    outputArray = [[1, 1, 1, 1, -1, 1, 1, -1, 1],
                   [1, -1, 1, 1, 1, -1, 1, -1, 1]]
    testArray = [[1, 1, -1, 1, -1, 1, -1, -1, 1, -1, 1, 1, -1, -1, -1, 1], 
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    Cosco(inputArray, outputArray, testArray)
main()