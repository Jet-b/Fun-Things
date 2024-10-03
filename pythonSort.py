from time import perf_counter
from random import randrange
import matplotlib.pyplot as plt


def time_n(n):
    lst = [randrange(10000) for i in range(n)]
    start = perf_counter()
    sorted(lst)
    return perf_counter() - start

times = []
for n in range(1, 15000):
    if n % 1000 == 0:
        print(n)
    times.append(time_n(n))

plt.plot([i+1 for i in range(len(times))], times)

plt.show()