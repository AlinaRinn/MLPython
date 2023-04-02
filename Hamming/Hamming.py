import Common
from PIL import Image
from numpy import array

def imageRecognizer(filename):
    img = Image.open(filename)
    img  = img.convert('1')
    return list(array(img))

def binArrayParser(array):
    returnArray = list()
    for i in array:     
        for j in i:
            if (j == False):
                returnArray.append(1)
            elif (j == True):
                returnArray.append(-1)
    return returnArray

def Hamming(X, Xn): 
    print(X)
    W = list(Common.multiplier(X, 0.5))
    print(W)
    T = len(W[0]) / 2
    eps = 1 / len(X)
    E = [[-eps for j in range(len(X))] for i in range(len(X))]
    E = Common.diagonalNullifier(E, 1)
    print(E)
    Emax = 0.1
    for e in range(len(Xn)):
        print("\nImage", e)
        S1 = Common.summator(Common.multiply(W, Common.transpose([Xn[e]])), T)
        Y1 = list([[Common.LinearThreshold(S1[i][0], T) for i in range(len(S1))]])
        print("S1:", S1, "\n\nY1:", Y1, "\n2")
        Y2 = Y1
        Yprev = Y1
        check = 1
        counter = 0
        while(check >= Emax):
            print("\nIter ", counter, "\n----------------------------------------")
            Yprev = Y2
            S2 = Common.multiply(E, Common.transpose(Y2))
            Y2 = list([[Common.LinearThreshold(S2[i][0], T) for i in range(len(S2))]])
            check = sum(Common.powList(Common.difference2dim(Y2, Yprev)))
            counter += 1
            print("S2: ", S2, "\nY2", Y2, "\n", "Check: ", check)
        print("Match to training image", Y2[0].index(max(Y2[0])))
        
        
def main(): 
    #inputArray = [[1, -1, 1, -1, 1, -1, 1, -1, 1],
    #              [-1, 1, -1, 1, 1, 1, -1, 1, -1],
    #              [1, 1, 1, 1, -1, 1, 1, 1, 1]]
    #testArray = [[1, -1, -1, -1, 1, -1, 1, -1, 1], 
    #             [1, 1, 1, -1, -1, -1, 1, 1, 1]]
    inputArray = list()
    testArray = list()
    inputArray.append(binArrayParser(imageRecognizer('mono128x128/img3.bmp')))
    inputArray.append(binArrayParser(imageRecognizer('mono128x128/img4.bmp')))
    inputArray.append(binArrayParser(imageRecognizer('mono128x128/img5.bmp')))
    testArray.append(binArrayParser(imageRecognizer('mono128x128/img3noisy.bmp')))
    testArray.append(binArrayParser(imageRecognizer('mono128x128/img4noisy.bmp')))
    testArray.append(binArrayParser(imageRecognizer('mono128x128/img5noisy.bmp')))
    #testArray.append(binArrayParser(imageRecognizer('mono128x128/img4mono.bmp')))

    Hamming(inputArray, testArray)
main()
