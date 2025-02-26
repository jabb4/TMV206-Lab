import numpy as np
from scipy import linalg as LA
from sympy import Matrix
import time

def solve_using_rref(matrix, vector_y=Matrix([[]])):
    matrix = Matrix(matrix)
    vector_y = Matrix(vector_y)
    trappstegsform = matrix.rref()[0]
    pivotelement = matrix.rref()[1]
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

    ## Check if the only solution is x=0
    if sum(list(map(lambda x: sum(x), beronde_vars))) == 0:
        return 0, "x = 0"

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
    
    if not fria_vars:
        for var in beronde_vars:
            pass

    alphbet_without_x = "abcdefghijklmnopqrstuvwyz"*100
    var_names = []
    index = 1
    for var in range(nr_colums):
        if not alphbet_without_x[var] + str(index) in var_names:
            var_names.append(alphbet_without_x[var] + str(index))
    
    print(max(list(map(lambda x: max(x, key=lambda x: len(str(x))), fria_vars)), lambda x: len(x)))
    nice_string = []
    #max_row_len = len(str(max(list(map(lambda x: max(x, key=lambda x: len(str(x))), fria_vars)),lambda x:len(str(x)))))
    for row in range(nr_colums):
        tmp = ""
        for var in range(len(fria_vars)):
            if row == round(nr_colums/2):
                if var == 0:
                    tmp += f"x =   {var_names[var]} "
                else:
                    tmp += f"   +  {var_names[var]} "
            else:
                tmp += "         "
            row_len = len(str(fria_vars[var][row]))
            if row_len == max_row_len:
                tmp += f"( {fria_vars[var][row]} )"
            elif (max_row_len - row_len) % 2 == 1:
                tmp += f"( {(round(max_row_len/2)-1)*" "}{fria_vars[var][row]}{(round(max_row_len/2)-2)*" "} )"
            else:
                tmp += f"( {(round(max_row_len/2)-1)*" "}{fria_vars[var][row]}{(round(max_row_len/2)-1)*" "} )"
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
    print("Uppgift A:")
    for line in solve_using_rref(A)[1]:
        print(line)
    print("\n\n")


def uppgiftB(A, y, Aint, yint):
    print("Uppgift B med rand():")
    t=time.time()
    print(solve_using_rref(A, y)[1])
    print("Time taken on rand():", time.time()-t, "\n\n")

    print("Uppgift B med randint():")
    t=time.time()
    print(solve_using_rref(Aint, yint)[1])
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
    A = np.random.rand(100, 100)
    Aint = np.random.randint(0, 100, size=(100, 100))

    y = np.random.rand(100)
    yint = np.random.randint(0, 100, size=(100))

    uppgiftA()
    #uppgiftB(A, y, Aint, yint)
    #uppgiftC(A, y, Aint, yint)

if __name__ == "__main__":
    main()
