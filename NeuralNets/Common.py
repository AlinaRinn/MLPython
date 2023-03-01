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

def NumerizedPrint(array):
    for i in range(len(array)):
        print("%3d) %s" % (i, array[i]))