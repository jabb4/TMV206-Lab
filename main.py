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

print(fraktaler(np.array([[1,2],[1,2]]), np.array([1,2]),2))
