import numpy as np

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

def delb():
    A1 = np.array([[0, 0], [0, 0.16]])
    A2 = np.array([[0.85, 0.04], [-0.04, 0.85]])
    A3 = np.array([[0.2, -0.26], [0.23, 0.22]])
    A4 = np.array([[-0.15, 0.28], [0.26, 0.24]])

    b1 = np.array([0, 0])
    b2 = np.array([0, 1.6])
    b3 = np.array([0, 1.6])
    b4 = np.array([0, 0.44])
