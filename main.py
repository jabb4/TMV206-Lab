import numpy as np
import random

"""
Gör något IFS fraktal
args:
A: 2 x 2 matris
v0: en vektor
n: heltal >= 1
"""
def fraktaler(A, v0, n):
    result = np.zeros((2, n))
    result[:,0] = v0

    for k in range(1,n):
        result[:,k] = A@result[:,k-1]
    
    return result

def delb(A, v0, n):
    A1 = np.array([[0, 0], [0, 0.16]])
    A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
    A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
    A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])

    b1 = np.array([0, 0])
    b2 = np.array([0, 1.6])
    b3 = np.array([0, 1.6])
    b4 = np.array([0, 0.44])

    result = np.zeros((2, n))
    result[:,0] = v0

    for k in range(1,n):
        index = random.randrange(1, 100)
        b = np.zeros((1, 1))
        
        if index == 1:
            b = b1
            A = A1
        elif index >= 2 and index < 86:
            b = b2
            A = A2
        elif index >= 86 and index < 94:
            b = b3
            A = A3
        elif index >= 94 and index <= 100:
            b = b4
            A = A4

        result[:,k] = A@result[:,k-1] + b
    
    return result


print(fraktaler(np.array([[1,2],[1,2]]), np.array([1,2]),2))


index = random.randrange(1, 100)

if index == 1:
    A = A1
elif index >= 2 and index < 86:
    A = A2
elif index >= 86 and index < 94:
    A = A3
elif index >= 94 and index <= 100:
    A = A4