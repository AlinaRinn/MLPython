import Common

def Hopfield(X, Xprac):
    print("X:", Common.NumerizedPrint(X))
    W = Common.multiply(Common.transpose(X), X)
    W = Common.diagonalNullifier(W)
    print("W:\n", Common.NumerizedPrint(W))

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
            temp = [] 
            for j in range(len(Y[0])): # 2.3
                temp.append(Common.SingleJump(S[j], 0))
            Y.append(temp)
            print("Y1:\n", Y[counter+1])   
            n = sum(Common.powList(Common.difference(Y[counter], Y[counter+1]))) # 2.4
            print("n:", n)
            if(counter > 1 and sum(Common.powList(Common.difference(Y[counter], Y[counter - 2]))) == 0 and sum(Common.powList(Common.difference(Y[counter - 1], Y[counter - 3]))) == 0):
                print("This image not recognized:\n", Y[counter])  
                break
            counter += 1

def main():
    InputArray = [[1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 # NxM
                  [1, 1, 1, 1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1]] # 2 
    Practice =   [[1, 1, 1, -1, 1, -1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1], # 1 mod
                  [1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, 1, 1]] # 2 mod
    Hopfield(InputArray, Practice)
main()