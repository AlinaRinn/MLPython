from RadiallySymmetric import Gauss
import numpy as np

def main():
    InputArray = [[-2.0, -0.48], 
                  [-1.5, -0.78], 
                  [-1.0, -0.83], 
                  [-0.5, -0.67], 
                  [0.0, -0.20], 
                  [0.5, 0.70], 
                  [1.0, 1.48], 
                  [1.5, 1.17], 
                  [2.0, 0.20]]
    a = np.array(InputArray, float)
    a = a.T
    print(a)
    Gauss(a)

main()
