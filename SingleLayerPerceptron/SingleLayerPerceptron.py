import random

def Taubin(x, y, z):
    return (x**2 + 9*y**2/4 + z**2 - 1)**3 - x**2*z**3 - 9*y**2*z**3/80

def RandomFill(a, b, c, d):
    for i in range(b):
        a.append([random.randint(c, d), random.randint(c, d), random.randint(c, d), 0])
        a[i][3] = Taubin(a[i][0], a[i][1], a[i][2])

def NumerizedPrint(a):
    for i in range(len(a)):
        print("%3d) %s" % (i, a[i]))

def Uniqulizer(a):
    print("\nInput array length:", len(a), "\n")
    NumerizedPrint(a)   
    b = []

    # First correction
    a.sort(key = lambda x: (x[0], x[1]))
    print("\nSorted array(0, 1):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if(a[i][0] == a[i+1][0] and a[i][1] == a[i+1][1]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML model:", b)
    for i in reversed(range(len(b))):
        del(a[b[i]])
    b.clear()

    # Last correction
    a.sort(key = lambda x: (x[1], x[2]))
    print("\nSorted array(1, 2):")
    NumerizedPrint(a)
    for i in range(0, len(a) - 1, 1):
        if(a[i][1] == a[i+1][1] and a[i][2] == a[i+1][2]):
            b.append(i)

    print("\nThis array units will been deleted for improving ML data:", b)
    for i in reversed(range(len(b))):
        del(a[b[i]])

    print("\nFinal array view:")
    NumerizedPrint(a)


def main():
    InputList = []
    RandomFill(InputList, 100, -10, 10)
    Uniqulizer(InputList)


main()