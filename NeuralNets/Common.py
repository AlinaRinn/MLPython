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


### Common use functions ###

random.seed(5)
def RandomFill(array, size, rangeMin, rangeMax):
    for i in range(size):
        array.append([random.randint(rangeMin, rangeMax), random.randint(rangeMin, rangeMax), random.randint(rangeMin, rangeMax), 0])
        array[i][3] = Simple(array[i][0], array[i][1], array[i][2])

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

def FloatNumerizedPrint(array, roundsigns):
    for i in range(len(array)):
        print("%3d)" % i, end=" ")
        for j in range(len(array[0])):
            print(round(array[i][j], roundsigns), end=" ")
        print("\n", end="")