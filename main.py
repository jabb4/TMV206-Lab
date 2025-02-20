import numpy as np
import matplotlib.pyplot as plt

def UppgiftA(V0, n):
    A = np.matrix([[0.7, 0.1, 0.3], [0.1, 0.6, 0.2], [0.2, 0.3, 0.5]])

    poweredA = np.linalg.matrix_power(A, n)
    
    result = poweredA @ V0
    return result

def UppgiftB():
    n = range(1,10)
    
    C0 = 333
    L0 = 333
    U0 = 333
    V0 = np.matrix([[C0], [L0], [U0]])
    plt.figure(figsize=(10,6))
    plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=0.9, wspace=0.7, hspace=0.6)
    plt.subplot(3, 3, 2)
    plt.title("1/3 per, v:1-10")
    plt.ylabel("Bilar")
    plt.plot(n, [round(float(UppgiftA(V0, x)[0])) for x in n], label="Centralen")
    plt.plot(n, [round(float(UppgiftA(V0, x)[1])) for x in n], label="Landvetter")
    plt.plot(n, [round(float(UppgiftA(V0, x)[2])) for x in n], label="Uthyrda")
    plt.legend(bbox_to_anchor=(1.7, 0.4, 0.5, 0.5))

    plt.subplot(3, 3, 4)
    plt.title("Bara Centralen, v:1-10")
    plt.ylabel("Bilar")
    C0 = 999
    L0 = 0
    U0 = 0
    V0 = np.matrix([[C0], [L0], [U0]])
    print([float(UppgiftA(V0, x)[0]) for x in n])
    plt.plot(n, [round(float(UppgiftA(V0, x)[0])) for x in n], label="Centralen")
    plt.plot(n, [round(float(UppgiftA(V0, x)[1])) for x in n], label="Landvetter")
    plt.plot(n, [round(float(UppgiftA(V0, x)[2])) for x in n], label="Uthyrda")

    plt.subplot(3, 3, 5)
    plt.title("Bara Landvetter, v:1-10")
    C0 = 0
    L0 = 999
    U0 = 0
    V0 = np.matrix([[C0], [L0], [U0]])
    print([float(UppgiftA(V0, x)[0]) for x in n])
    plt.plot(n, [round(float(UppgiftA(V0, x)[0])) for x in n], label="Centralen")
    plt.plot(n, [round(float(UppgiftA(V0, x)[1])) for x in n], label="Landvetter")
    plt.plot(n, [round(float(UppgiftA(V0, x)[2])) for x in n], label="Uthyrda")

    plt.subplot(3, 3, 6)
    plt.title("Bara Uthyrning, v:1-10")
    C0 = 0
    L0 = 0
    U0 = 999
    V0 = np.matrix([[C0], [L0], [U0]])
    print([float(UppgiftA(V0, x)[0]) for x in n])
    plt.plot(n, [round(float(UppgiftA(V0, x)[0])) for x in n], label="Centralen")
    plt.plot(n, [round(float(UppgiftA(V0, x)[1])) for x in n], label="Landvetter")
    plt.plot(n, [round(float(UppgiftA(V0, x)[2])) for x in n], label="Uthyrda")

    n = [1, 10, 100, 1000, 10000, 100000]
    plt.subplot(3, 3, 7)
    plt.title("Bara Centralen, v:1-100000")
    plt.xlabel("Veckor")
    plt.ylabel("Bilar")
    C0 = 999
    L0 = 0
    U0 = 0
    V0 = np.matrix([[C0], [L0], [U0]])
    print([float(UppgiftA(V0, x)[0]) for x in n])
    plt.plot(n, [round(float(UppgiftA(V0, x)[0])) for x in n], label="Centralen")
    plt.plot(n, [round(float(UppgiftA(V0, x)[1])) for x in n], label="Landvetter")
    plt.plot(n, [round(float(UppgiftA(V0, x)[2])) for x in n], label="Uthyrda")

    plt.subplot(3, 3, 8)
    plt.title("Bara Landvetter, v:1-100000")
    plt.xlabel("Veckor")
    C0 = 0
    L0 = 999
    U0 = 0
    V0 = np.matrix([[C0], [L0], [U0]])
    print([float(UppgiftA(V0, x)[0]) for x in n])
    plt.plot(n, [round(float(UppgiftA(V0, x)[0])) for x in n], label="Centralen")
    plt.plot(n, [round(float(UppgiftA(V0, x)[1])) for x in n], label="Landvetter")
    plt.plot(n, [round(float(UppgiftA(V0, x)[2])) for x in n], label="Uthyrda")

    plt.subplot(3, 3, 9)
    plt.xlabel("Veckor")
    plt.title("Bara Uthyrda, v:1-100000")
    C0 = 0
    L0 = 0
    U0 = 999
    V0 = np.matrix([[C0], [L0], [U0]])
    print([float(UppgiftA(V0, x)[0]) for x in n])
    print([float(UppgiftA(V0, x)[1]) for x in n])
    print([float(UppgiftA(V0, x)[2]) for x in n])
    plt.plot(n, [round(float(UppgiftA(V0, x)[0])) for x in n], label="Centralen")
    plt.plot(n, [round(float(UppgiftA(V0, x)[1])) for x in n], label="Landvetter")
    plt.plot(n, [round(float(UppgiftA(V0, x)[2])) for x in n], label="Uthyrda")


    plt.show()



UppgiftB()

C0 = 31
L0 = 42
U0 = 35
n = 10
V0 = np.matrix([[C0], [L0], [U0]])

print(f"V{n} = {UppgiftA(V0, n)} \n")



#Vid fallet där C0 = L0 = U0 = B, där B tillhör naturliga talen, kommer resulterande matris Vn förbli V0; Vn = V0
