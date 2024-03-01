from random import randint
from math import sqrt


def listmaker():
    for i in range(100):
        x.append(randint(-100,100))
        y.append(randint(-100,100))

def checkiftriangle():
    for i in range(1,100):
        for j in range(1,100):
            for k in range(1,100):
                if(i==j or i== k or j == k):
                    continue
                a = getdistance(x[i], y[i], x[j], y[j])
                b = getdistance(x[i], y[i], x[k], y[k])
                c = getdistance(x[j], y[j], x[k], y[k])

                s = (a+b+c) / 2
                A = sqrt(s * (s - a) * (s - b) * (s - c))
                if(A < 0): continue
                else:
                    print(A)

def getdistance(firstx,firsty,secondx,secondy):
    dist = sqrt((secondx - firstx)**2 + (secondy - firsty)**2)
    return dist

x = []
y = []
listmaker()
checkiftriangle()


