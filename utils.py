from random import randint
from math import sqrt


def listmaker():
    for i in range(100):
        x.append(randint(-100,100))
        y.append(randint(-100,100))

def checkiftriangle():
    sum = 0
    for i in range(100):         ##exei problima o deiktis
        for j in range(i+1,100):
            for k in range(j+1,100):
                if(i==j or i== k or j == k):
                    continue
                a = getdistance(x[i], y[i], x[j], y[j])
                b = getdistance(x[i], y[i], x[k], y[k])
                c = getdistance(x[j], y[j], x[k], y[k])

                
                s = (a+b+c) / 2
                area_squared = s * (s - a) * (s - b) * (s - c)

                if area_squared < 0:
                    continue

                A = area_squared ** 0.5
                if A > 0:
                    sum += 1

    return sum

def getdistance(firstx,firsty,secondx,secondy):
    dist = sqrt((secondx - firstx)**2 + (secondy - firsty)**2)
    return dist

def mesos(li):
    sum = 0
    for i in li:
        sum += i
    return sum/len(li)
        
def diamesos(li):
    l = li.sort()
    x = len(li) // 2
    return li[x]

def evros(li):
    l = li.sort()
    x = len(li)
    if(li[0] > li[x-1]):
        return li[0] - li[x-1]
    else:
        return li[x-1] - li[0]
    
def apoklisi(li):
    mesos_value = mesos(li)
    sum_squared_diff = sum((i - mesos_value) ** 2 for i in li)
    mesos2 = sum_squared_diff / len(li)
    standard_deviation = sqrt(mesos2)
    
    return standard_deviation


x = []
y = []
listmaker()
p =checkiftriangle()
print("Mporoun na ftiaxtoun: "  + str(p) + " Trigona")


list1 = [6,5,4.3,6,8,7,6,4,9,7,66,77,88,222,11,33,44,5,3,33,44,555]

print("O mesos einai: " + str(mesos(list1)))
print("H diamesos einai: " + str(diamesos(list1)))
print("To evros einai: " + str(evros(list1)))
print("H apoklisi einai: " + str(apoklisi(list1)))