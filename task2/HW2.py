import math


def histDistance(hist1, hist2) -> float:
    summary = 0.0
    for i in range(len(hist1)):
        summary = summary + (hist1[i] - hist2[i]) ** 2
    print("The distance between histograms is ",math.sqrt(summary))


def triangle(a):
    count = 0
    while count <= a:
        print(" " * (a - count + 1) + "*" + "*" * count * 2)
        count += 1


def writeInFile(filename, hist):
    n = open(filename, "a")
    n.write(str(hist))
    n.close()
    print("Written successfully")


def readFile(filename):
    n = open(filename, "r")
    for i in n:
        print(i)
    n.close()


triangle(3)
histDistance([1, 3, 8, 10], [1, 8, 10, 10])
writeInFile("testfile", [1, 2, 2, 5, 5, 5])
readFile("testfile")
