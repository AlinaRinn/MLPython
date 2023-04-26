import random
E = 2.7182818284590452353602874713526624977572470936999595749669676277240766303

### Input generation functions ###

def Taubin(x, y, z):
    return (x**2 + 9*y**2/4 + z**2 - 1)**3 - x**2*z**3 - 9*y**2*z**3/80

def Simple(x, y, z):
    return x**3 - y**2 - z


### Activation functions ###

def SigmoidLogistics(A, S):   # A - feed parametr, S - neuron state
    return 1 / (E **(-A*S) + 1)

def SigmoidHyperbolicTan(A, S):   # Same
    return 2*SigmoidLogistics(A, S) - 1

def LinearThreshold(S, T):
    if (S <= 0):
        return 0
    elif (S > 0 and S <= T):
        return S
    elif (S >= T):
        return T

def SingleJump(S, T):
    if (S <= T):
        return -1
    elif (S > T):
        return 1

### Common use functions ###

def transpose(array):
    transposed = list()
    for i in range(len(array[0])):
        row = list()
        for sublist in array:
            row.append(sublist[i])
        transposed.append(row)
    return transposed

def multiply(array0, array1, adding = 0):
    multiplied = []
    counter = len(array0)
    for k in range(len(array0)):
        stringsum = []
        for i in range(len(array1[0])):
            string = 0
            for j in range(len(array0[0])):
                string += array0[k][j]*array1[j][i] + adding
            stringsum.append(string)
        if ((k % 100) == 0): 
            print(k, " from", counter)
        multiplied.append(stringsum.copy())
    return multiplied

def multiplier(array, mult):
    multi = array
    for i in range(len(multi)):
       for j in range(len(multi[0])):
          multi[i][j] = multi[i][j]*mult
    return multi

def summator(array, summ):
    result = array
    for i in range(len(result)):
       for j in range(len(result[0])):
          result[i][j] = result[i][j] + summ
    return result

def diagonalNullifier(array, replace = 0):
    nullified = array
    for i in range(len(nullified)):
        for j in range(len(nullified[0])):
            if(i == j):
                nullified[i][j] = replace
    return nullified

def difference(array0, array1):
    diff = list()
    for i in range(len(array0)):
        diff.append(array0[i] - array1[i])
    return diff

def difference2dim(array0, array1):
    diff = list()
    for i in range(len(array0)):
        for j in range(len(array0[0])):
            diff.append(array0[i][j] - array1[i][j])
    return diff

def dim2to1(array0):
    dim = list()
    for i in range(len(array0)):
        for j in range(len(array0[0])):
            dim.append(array0[i][j])
    return dim

def powList(array: list) -> list:
    powList = array
    for i in range(len(powList)):
        powList[i] = powList[i]**2
    return powList

def randomFill(arrayLenght, rangeMin, rangeMax, sizeX = 3, sizeY = 1): 
    randomArray = list()
    for i in range(arrayLenght):
        string = list()
        for j in range(sizeX):
            string.append(random.randint(rangeMin, rangeMax))
        for j in range(sizeY):
            string.append(Simple(string[0], string[1], string[2]))
        randomArray.append(string)
    return randomArray

def Normalize(array, minmax):   # Array [x1, x2, x2, xn, y], minmax [min, max]
    for i in range(len(array)):
        for k in range(len(array[0]) - 1):
            array[i][k] = (array[i][k] - minmax[k][0]) / (minmax[k][1] - minmax[k][0])
        array[i][3] = (array[i][3] - minmax[3][0]) / (minmax[3][1] - minmax[3][0])

    print("\nNormalzed data: \n")
    NumerizedPrint(array)

def UniqulizeMinMax(a, minmax):
    print("\nInput array length:", len(a), "\n")
    NumerizedPrint(a)
    b = []

    # First correction
    a.sort(key=lambda x: (x[0], x[1]))
    minmax.append([a[0][0], a[len(a) - 1][0]])
    print("\nSorted array(0, 1):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if (a[i][0] == a[i + 1][0] and a[i][1] == a[i + 1][1]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML data:", b)
    for i in reversed(range(len(b))):
        del (a[b[i]])
    b.clear()
    
    # Last correction
    a.sort(key=lambda x: (x[1], x[2]))
    minmax.append([a[0][1], a[len(a) - 1][1]])
    print("\nSorted array(1, 2):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if (a[i][1] == a[i + 1][1] and a[i][2] == a[i + 1][2]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML data:", b)
    for i in reversed(range(len(b))):
        del (a[b[i]])

    a.sort(key=lambda x: x[2])
    minmax.append([a[0][2], a[len(a) - 1][2]])
    a.sort(key=lambda x: x[3])
    minmax.append([a[0][3], a[len(a) - 1][3]])
    print("\nFinal array view:")
    NumerizedPrint(a)
    print("\nMin Max :", minmax)

def NumerizedPrint(array, end = "\n"):
    for i in range(len(array)):
        print("%3d) %s" % (i, array[i]), end=end)

def NumerizedFilePrint(array, f):
    counter = 0
    for line in array:
        f.write(f"{counter}){line}\n")
        counter += 1

def FloatNumerizedPrint(array, roundsigns):
    for i in range(len(array)):
        print("%3d)" % i, end=" ")
        for j in range(len(array[0])):
            print(round(array[i][j], roundsigns), end=" ")
        print("\n", end="")

