import numpy as np

C0 = 31
L0 = 42
U0 = 35
n = 10
V0 = np.matrix([[C0], [L0], [U0]])

"""
def ARecursive(C0, L0, U0, n):
    index = 0
    A = np.array([[0.7, 0.1, 0.2], [0.1, 0.6, 0.3], [0.3, 0.2, 0.5]])
    Vn_1 = np.array([[C0], [L0], [U0]])

    while (index < n):

        Vn = A @ Vn_1
        Vn_1 = Vn
        
        index += 1
        print(str(Vn) + "\n")

    print ("Slutgiltig matris: " + str(Vn))
"""

def UppgiftA(V0, n):
    A = np.matrix([[0.7, 0.1, 0.2], [0.1, 0.6, 0.3], [0.3, 0.2, 0.5]])
    print(f"A = {str(A)} \n")
    print(f"V0 = {str(V0)} \n")

    poweredA = np.linalg.matrix_power(A, n)
    
    result = poweredA @ V0
    print(f"V{n}= {str(result)} \n")

def UppgiftB():
    print(f"1 vecka: ")



#ARecursive(C0, L0, U0, n)
UppgiftA(V0, n)

#Vid fallet där C0 = L0 = U0 = B, där B tillhör naturliga talen, kommer resulterande matris Vn förbli V0; Vn = V0
