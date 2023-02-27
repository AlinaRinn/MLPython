from SingleLayerPerceptron import *

def main():
    InputList = []
    minmax = []
    RandomFill(InputList, 10, -10, 10)
    UniqulizeMinMax(InputList, minmax)
    Normalize(InputList, minmax)
    SingleLayerPerceptron(len(InputList[0]) - 1, len(InputList), 1, 0.99, InputList, 50)

main()
