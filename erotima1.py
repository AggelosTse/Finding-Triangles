from math import sqrt
from statistics import mean, median, stdev

def checkiftriangle():
    count = 0
    for i in range(100):  ##takes every possible 3 points combinations of these lists.
        for j in range(i + 1, 100):
            for k in range(j + 1, 100):
                if i == j or i == k or j == k:
                    continue
                a = getdistance(x[i], y[i], x[j], y[j])     ##calculates the distances between them.
                b = getdistance(x[i], y[i], x[k], y[k])
                c = getdistance(x[j], y[j], x[k], y[k])

                s = (a + b + c) / 2
                area_squared = s * (s - a) * (s - b) * (s - c)

                if area_squared < 0:
                    continue

                A = area_squared**0.5
                if A > 0:
                    count = count + 1
                    area.append(A)
    return count


def getdistance(firstx, firsty, secondx, secondy):  ##function that returns the distance between 2 points.
    distance = sqrt((secondx - firstx) ** 2 + (secondy - firsty) ** 2)
    return distance


area = []
points = "/home/angelo/Downloads/points.txt"

x = []
y = []


with open(points, "r") as file:     #opens the txt file.
    for line in file:
        columns = line.split()  # Splits the line into two columns.

        x.append(int(columns[0]))   #adds the first column of the file in a x list.
        y.append(int(columns[1]))   #adds the second column of the file in a y list.


possible_triangles = checkiftriangle()

mea = mean(area)
med = median(area)
deviation = stdev(area)

print(possible_triangles, mea, med, deviation)




