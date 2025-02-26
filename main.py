import numpy as np
from scipy import linalg as LA
from sympy import Matrix 
import time
    
def uppgiftA():
    A = Matrix([[1, 2, 1, -1, 2], [3, 4, 5, 2, 0], [2, 2, 1, 0, 2]])

    print(f"A: {A} \n")

    Arref = A.rref()

    print(f"A after rref: {Arref} \n")

    #Använder reslutatet av A.rref() för att få ut:
    #X1 = (-X4)
    #X2 = (3/2)(X4) - (5/3)(X5)
    #X3 = (4/3)(X5) - (X4)

    #Anta att X4 = t, och X5 = s

    #Ifrån detta får vi att X = t * ([[-1], [3/2], [-1], [1], [0]]) + s * ([[0], [-5/3], [4/3], [0], [1]])

    print("X = t * ([[-1], [3/2], [-1], [1], [0]]) + s * ([[0], [-5/3], [4/3], [0], [1]])")

uppgiftA()



def uppgiftB():
    