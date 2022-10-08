import random
import time


def calcHist(tdata):
    hist = [0] * 10
    for b in tdata:
        tdata[b] = random.randint(0, 999)
        if 0 <= tdata[b] <= 99:
            hist[0] += 1
        elif 100 <= tdata[b] <= 199:
            hist[1] += 1
        elif 200 <= tdata[b] <= 299:
            hist[2] += 1
        elif 300 <= tdata[b] <= 399:
            hist[3] += 1
        elif 400 <= tdata[b] <= 499:
            hist[4] += 1
        elif 500 <= tdata[b] <= 599:
            hist[5] += 1
        elif 600 <= tdata[b] <= 699:
            hist[6] += 1
        elif 700 <= tdata[b] <= 799:
            hist[7] += 1
        elif 800 <= tdata[b] <= 899:
            hist[8] += 1
        elif 900 <= tdata[b] <= 999:
            hist[9] += 1
    return hist


data = [0]*1000000

start = time.time()

num = 0
minimum = 99999999
maximum = 0
total = 0
timelist = [0]*100
while num < 100:
    start = time.time()
    d = calcHist(data)
    end = time.time()
    timelist[num] = (end - start)
    num += 1
    total += (end-start)

print(timelist)
average = total/100

print("Minimum time is", min(timelist))
print("Average time is", average)
print("Maximum time is", max(timelist))
