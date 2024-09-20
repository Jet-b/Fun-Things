from random import randrange, seed, choice
import matplotlib.pyplot as plt
from time import perf_counter
from os import system

system('cls')

def binary_search(lst, target):
    lst = sorted(lst)
    i1 = int(len(lst)/2)
    i2 = len(lst)-1
    while i1 != i2 and (abs(i1-i2) != 1):
        if lst[i1] == target:
            return i1
        elif lst[i1] < target:
            i1 = int((i1+i2)/2)
        else:
            i2 = i1
            i1 = int(i1/2)
    return None

x = []
y = []

for n in range(2,100):
    x.append(n)
    lst = sorted([randrange(1, 200) for _ in range(n)])
    lst.append(202)
    start = perf_counter()
    binary_search(lst, lst[-1])
    end = perf_counter()
    y.append(end-start)

plt.plot(x, y)
plt.show()