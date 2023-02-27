import random

random.seed(5)

def Taubin(x, y, z):
    return (x**2 + 9*y**2/4 + z**2 - 1)**3 - x**2*z**3 - 9*y**2*z**3/80

def Simple(x, y, z):
    return x**3 - y**2 - z

def RandomFill(array, size, rangeMin, rangeMax):
    for i in range(size):
        array.append([random.randint(rangeMin, rangeMax), random.randint(rangeMin, rangeMax), random.randint(rangeMin, rangeMax), 0])
        array[i][3] = Taubin(array[i][0], array[i][1], array[i][2])

def NumerizedPrint(array):
    for i in range(len(array)):
        print("%3d) %s" % (i, array[i]))