from random import randint
from math import sqrt


def listmaker():
    for i in range(100):  # adds random values from -100 to 100 in the 2 lists.
        x.append(randint(-100, 100))
        y.append(randint(-100, 100))


def checkiftriangle():
    count = 0
    for i in range(100):  # takes every possible 3 points combinations of these lists.
        for j in range(i + 1, 100):
            for k in range(j + 1, 100):
                if i == j or i == k or j == k:
                    continue
                a = getdistance(
                    x[i], y[i], x[j], y[j]
                )  # calculates the distances between them.
                b = getdistance(x[i], y[i], x[k], y[k])
                c = getdistance(x[j], y[j], x[k], y[k])

                s = (a + b + c) / 2
                area_squared = s * (s - a) * (s - b) * (s - c)

                if area_squared < 0:
                    continue

                A = area_squared**0.5
                if A > 0:
                    count = count + 1
                    arealist.append(A)

    return count


def getdistance(firstx, firsty, secondx, secondy):  # function that returns the distance between 2 points.
    distance = sqrt((secondx - firstx) ** 2 + (secondy - firsty) ** 2)
    return distance


def findmean(li):  # finds mean value from the random list.
    return sum(li) / len(li)


def findmedian(li):  # finds median value from the random list.
    l = li.sort()
    x = len(li) // 2    #takes the middle element of the list.
    return li[x]


def findrange(li):  # finds range value from the random list.
    l = li.sort()
    x = len(li)
    if li[0] > li[x - 1]:
        return li[0] - li[x - 1]
    else:
        return li[x - 1] - li[0]


def findstdev(li):  # finds standard deviation from the random list.
    mean_value = findmean(li)
    sum_squared_diff = sum((i - mean_value) ** 2 for i in li)
    mean_value2 = sum_squared_diff / len(li)
    standard_deviation = sqrt(mean_value2)

    return standard_deviation


x = []
y = []
arealist = []       #list with all the triangle arias.


listmaker()  # creates 2 lists,for the x and y values.
possible_triangles = checkiftriangle()  # returns the number of triangles that can be created from all 3 possible combinations.
print(str(possible_triangles) + " Possible triangles can be made.")


print("Mean value is: " + str(findmean(arealist)))
print("Median value is: " + str(findmedian(arealist)))
print("Range value is: " + str(findrange(arealist)))
print("Standard deviation is: " + str(findstdev(arealist)))
