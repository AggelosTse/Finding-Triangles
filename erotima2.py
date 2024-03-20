from math import sqrt
from statistics import mean, median, stdev


def checkiftriangle():
    sum = 0
    for i in range(100):  ##exei problima o deiktis
        for j in range(i + 1, 100):
            for k in range(j + 1, 100):
                if i == j or i == k or j == k:
                    continue
                a = getdistance(x[i], y[i], x[j], y[j])
                b = getdistance(x[i], y[i], x[k], y[k])
                c = getdistance(x[j], y[j], x[k], y[k])

                s = (a + b + c) / 2
                area_squared = s * (s - a) * (s - b) * (s - c)

                if area_squared < 0:
                    continue

                A = area_squared**0.5
                if A > 0:
                    sum = sum + 1
                    embadon.append(A)
    return sum


def getdistance(firstx, firsty, secondx, secondy):
    dist = sqrt((secondx - firstx) ** 2 + (secondy - firsty) ** 2)
    return dist


embadon = []
points = "/home/angelo/Downloads/points.txt"

x = []
y = []


with open(points, "r") as file:
    for line in file:
        # Split the line into two columns based on a delimiter (e.g., space or tab)
        columns = line.split()

        # Assuming two columns, convert each column to a float and append to the respective lists
        x.append(int(columns[0]))
        y.append(int(columns[1]))


p = checkiftriangle()

mea = mean(embadon)
med = median(embadon)
deviation = stdev(embadon)

print(p, mea, med, deviation)
