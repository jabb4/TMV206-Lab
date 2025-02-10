import numpy as np

def skalarprodukt(u, v):
    return np.dot(u, v)

def korsprodukt(u, v):
    return np.cross(u, v)

def projektion(P, normalvektor=None, uplan=None,  vplan=None):
    v = np.array([0,0,0]) - P
    try:
        normalvektor.all()
    except:
        normalvektor = korsprodukt(uplan ,vplan)

    v2 = (skalarprodukt(v,normalvektor)/skalarprodukt(normalvektor,normalvektor))*normalvektor
    v1 = v - v2

    return v1

def b():
    u = np.array([1,1,0])
    v = np.array([0,-1,0])
    P = np.array([np.pi, np.e, 1])

    print("u, v: " + str(projektion(P,None,u,v)))
    print("u, -v: " + str(projektion(P,None,u,-v)))

def c():
    n = np.array([1,1,1])
    m = np.array([3,3,3])
    P = np.array([np.pi, np.e, 1])

    print("n: " + str(projektion(P,n)))
    print("m: " + str(projektion(P,m)))

b()
c()

# Vi använder oss av formeln U x V för att få normalvektorn till planet som spänns upp utav U och V
# Sen när vi har normalvektorn till planet kan vi använda formeln v2 = (v * normalvektorn / v * v)normalvektorn ,där v är vektorn från origo till punkt P och v2 är vektorn som är vinkelrät med planet och som går till våran punkt P.
# Sen när vi har v2 så använder vi formeln v1 = v - v2, där v1 då är vår projektion
# Vi ser att resultatet blir densamma i de två fallen i a och samma för de två fallen i b. Detta för att det är samma plan.