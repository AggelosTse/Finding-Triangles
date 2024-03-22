from random import randint
from math import sqrt


def listmaker():
    for i in range(100):                #adds random values from -100 to 100 in the 2 lists.
        x.append(randint(-100, 100))        
        y.append(randint(-100, 100))


def checkiftriangle():
    count = 0
    for i in range(100):            #takes every possible 3 points combinations of these lists.
        for j in range(i + 1, 100):
            for k in range(j + 1, 100):
                if i == j or i == k or j == k:
                    continue
                a = getdistance(x[i], y[i], x[j], y[j])     #calculates the distances between them.
                b = getdistance(x[i], y[i], x[k], y[k])
                c = getdistance(x[j], y[j], x[k], y[k])

                s = (a + b + c) / 2
                area_squared = s * (s - a) * (s - b) * (s - c)

                if area_squared < 0:        
                    continue

                A = area_squared**0.5
                if A > 0:
                    count = count + 1

    return count


def getdistance(firstx, firsty, secondx, secondy):  #function that returns the distance between 2 points.
    distance = sqrt((secondx - firstx) ** 2 + (secondy - firsty) ** 2)
    return distance


def findmean(li):      #finds mean value from the random list.
    sum = 0
    for i in li:
        sum += i
    return sum / len(li)


def findmedian(li):   #finds median value from the random list.
    l = li.sort()
    x = len(li) // 2
    return li[x]


def findrange(li):      #finds range value from the random list.
    l = li.sort()
    x = len(li)
    if li[0] > li[x - 1]:
        return li[0] - li[x - 1]
    else:
        return li[x - 1] - li[0]


def findstdev(li):      #finds standard deviation from the random list.
    mean_value = findmean(li)
    sum_squared_diff = sum((i - mean_value) ** 2 for i in li)
    mean_value2 = sum_squared_diff / len(li)
    standard_deviation = sqrt(mean_value2)

    return standard_deviation


x = []
y = []
listmaker() #creates 2 lists,for the x and y values.
possible_triangles = checkiftriangle()   #returns the number of triangles that can be created from all 3 possible combinations.
print(str(possible_triangles) + " Possible triangles can be made.")


list1 = [6, 5, 4.3, 6, 8, 7, 6, 4, 9, 7, 66, 77, 88, 222, 11, 33, 44, 5, 3, 33, 44, 555]

print("Mean value is: " + str(findmean(list1)))
print("Median value is: " + str(findmedian(list1)))
print("Range value is: " + str(findrange(list1)))
print("Standard deviation is: " + str(findstdev(list1)))
