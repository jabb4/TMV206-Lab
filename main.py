import numpy as np
from scipy import linalg as LA
from sympy import Matrix
import time

def solve_using_rref(matrix, vector_y):
    matrix = Matrix(matrix)
    vector_y = Matrix(vector_y)
    matrix = matrix.row_join(vector_y)
    trappstegsform, pivotelement = matrix.rref()
    nr_colums = len(trappstegsform.row(1))

    y_factor = []
    for i in range(nr_colums-1):
        if i in pivotelement:
            y_factor.append(trappstegsform.row(i)[-1])
        else:
            y_factor.append(0)

    beronde_vars = []
    for i1, e1 in enumerate(pivotelement):
        tmp = []

        for i2, e2 in enumerate(trappstegsform.row(i1)[:-1]):
            if i2 != e1:
                tmp.append(-e2)
            else:
                tmp.append(0)
        beronde_vars.append(tmp)


    fria_vars = []
    for varnr in range(len(beronde_vars),nr_colums-1):
        tmp = []
        for i in range(nr_colums-1):
            if i+1 <= len(beronde_vars):
                tmp.append(beronde_vars[i][varnr])
            elif i == varnr:
                tmp.append(1)
            else:
                tmp.append(0)
        fria_vars.append(tmp)


    alphbet_without_x = "abcdefghijklmnopqrstuvwyz"*100
    var_names = []
    index = 1
    for var in range(nr_colums):
        if not alphbet_without_x[var] + str(index) in var_names:
            var_names.append(alphbet_without_x[var] + str(index))

    nice_string = []
    ## Check if the only solution is x=0
    if sum(list(map(lambda x: sum(x), beronde_vars))) == 0:
        max_row_len = len(str(round(max(y_factor, key=lambda x: len(str(round(x,3)))), 3)))
        for i, e in enumerate(y_factor):
            tmp = ""
            if i+1 == round((len(y_factor)-1)/2):
                tmp += "  x  =  "
            else:
                tmp += "        "
            tmp += f"({str(round(e, 3)):^{max_row_len+1}})"
            nice_string.append(tmp)

        return y_factor, nice_string

    max_row_len = len(max(list(map(lambda x: str(max(x, key=lambda x: len(str(x)))), fria_vars)), key=lambda x: len(x)))

    for row in range(nr_colums-1):
        tmp = ""
        for var in range(len(fria_vars)+1):
            if var+1 != len(fria_vars)+1:
                if row == round((nr_colums-1)/2):
                    if var == 0:
                        tmp += f"x =  {var_names[var]} "
                    else:
                        tmp += f"  +  {var_names[var]} "
                else:
                    tmp += "        "
                tmp += f"({str(fria_vars[var][row]):^{max_row_len+1}})"

            elif max(y_factor) == 0 and min(y_factor) == 0:
                pass
            else:
                if row == round((nr_colums-1)/2):
                    tmp += f"  +   "
                else:
                    tmp += "      "
                tmp += f"({str(y_factor[row]):^{max_row_len+1}})"


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
    y = Matrix([[0], [0], [0]])
    print("Uppgift A:")
    for line in solve_using_rref(A, y)[1]:
        print(line)
    print("\n")


def uppgiftB(A, y, Aint, yint):
    print("Uppgift B med rand():")
    t=time.time()
    for line in solve_using_rref(A, y)[1]:
        print(line)
    print("Time taken on rand():", time.time()-t, "\n\n")

    print("Uppgift B med randint():")
    t=time.time()
    for line in solve_using_rref(Aint, yint)[1]:
        print(line)
    print("Time taken on randint():", time.time()-t, "\n\n")

def uppgiftC(A, y, Aint, yint):
    print("Uppgift C med rand():")
    t=time.time()
    solve_using_inverse(A, y)
    print("Using Inverse: Time taken on rand():", time.time()-t, "\n\n")

    print("Uppgift C med randint():")
    t=time.time()
    solve_using_inverse(Aint, yint)
    print("Time taken on randint():", time.time()-t)

def main():
    A = np.random.rand(5, 5)
    Aint = np.random.randint(0, 100, size=(5, 5))

    y = np.random.rand(5)
    yint = np.random.randint(0, 100, size=(5))

    uppgiftA()
    uppgiftB(A, y, Aint, yint)
    uppgiftC(A, y, Aint, yint)

if __name__ == "__main__":
    main()
