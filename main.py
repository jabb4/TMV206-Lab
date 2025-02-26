import numpy as np
from scipy import linalg as LA
from sympy import Matrix
import time

def solve_using_rref(matrix, vector_y=Matrix([[]])):
    matrix = Matrix(matrix)
    vector_y = Matrix(vector_y)
    trappstegsform = matrix.rref()[0]
    pivotelement = matrix.rref()[1]
    print(pivotelement)
    nr_rows = int(len(trappstegsform)/len(trappstegsform.row(1)))
    nr_colums = len(trappstegsform.row(1))

    beronde_vars = []
    for i1, e1 in enumerate(pivotelement):
        tmp = []
        for i2, e2 in enumerate(trappstegsform.row(i1)):
            if i2 != e1:
                tmp.append(-e2)
            else:
                tmp.append(0)
        beronde_vars.append(tmp)

    fria_vars = []
    for varnr in range(len(beronde_vars),nr_colums):
        tmp = []
        for i in range(nr_colums):
            if i+1 <= len(beronde_vars):
                tmp.append(beronde_vars[i][varnr])
            elif i == varnr:
                tmp.append(1)
            else:
                tmp.append(0)
        fria_vars.append(tmp)

    alphbet_without_x = "abcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyzabcdefghijklmnopqrstuvwyz"
    var_names = []
    index = 1
    for var in range(nr_colums):
        if not alphbet_without_x[var] + str(index) in var_names:
            var_names.append(alphbet_without_x[var] + str(index))
    
    nice_string = []
    for row in range(nr_colums):
        tmp = ""
        for var in range(len(fria_vars)):
            if row == round(nr_colums/2):
                tmp += f"   +  {var_names[var]} "
            else:
                tmp += "         "

            tmp += f"( {(3-round(len(str(fria_vars[var][row]))/4))*" "}{fria_vars[var][row]}{(3-round(len(str(fria_vars[var][row]))/4))*" "} )"
        if vector_y:
            if row == round(nr_colums/2):
                tmp += f"   -     "
            else:
                tmp += "         "
            tmp += f"( {(2-len(str(vector_y[row])))*" "}{vector_y[row]}{(2-len(str(vector_y[row])))*" "} )"
        nice_string.append(tmp)
    
    
    return fria_vars , nice_string

def solve_using_inverse(A, y):
    try:
        Ainv = LA.inv(A)
    except:
        print("A has no inverse")
        return None

    try: 
        Result = y @ Ainv
    except:
        print("A and y have mismatching dimensions")
        return None

    return Result

def uppgiftA():
    A = Matrix([[1,2,1,-1,2], [3,4,5,2,0], [2,2,1,0,2]])

    print(solve_using_rref(A)[0])
    for line in solve_using_rref(A)[1]:
        print(line)


def uppgiftB(A, y, Aint, yint):
    t=time.time()
    print(solve_using_rref(A, y)[0])
    print("Using rref: Time taken on rand():", time.time()-t)

    t=time.time()
    print(solve_using_rref(Aint, yint)[0])
    print("Using rref: Time taken on randint():", time.time()-t)

def uppgiftC(A, y, Aint, yint):
    t=time.time()
    solve_using_inverse(A, y)
    print("Using Inverse: Time taken on rand():", time.time()-t)

    t=time.time()
    solve_using_inverse(Aint, yint)
    print("Using Inverse: Time taken on randint():", time.time()-t)

def main():
    A = np.random.rand(100, 100)
    Aint = np.random.randint(0, 100, size=(100, 100))

    y = np.random.rand(100)
    yint = np.random.randint(0, 100, size=(100))

    uppgiftA()
    uppgiftB(A, y, Aint, yint)
    uppgiftC(A, y, Aint, yint)

if __name__ == "__main__":
    main()
