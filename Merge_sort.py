from random import randrange, shuffle
from time import perf_counter
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation#
import gc


def merge_sort(lst):
    # base case
    if len(lst) <= 1:
        return lst
    
    mid = len(lst) // 2
    
    # recur left and right
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    
    left_index = right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result += left[left_index:]
    result += right[right_index:]
    
    return result

def bogo_sort(lst):
    while lst != sorted(lst):
        shuffle(lst)
    return lst

def time_sort(sort_func, n):
    lst = [randrange(100) for i in range(n)]
    lst = sorted(lst)
    start = perf_counter()
    sort_func(lst)
    return perf_counter() - start

def plot_nlogn():
    pass

begin = 1000
lim = 3000

x = range(begin, lim)

merge_sort_times1 = []
for n in range(begin,lim):
    merge_sort_times1.append(time_sort(merge_sort, n))

plt.plot(x, merge_sort_times1, label="Merge Sort1", linestyle="-")

del merge_sort_times1
gc.collect()

merge_sort_times2 = []
for n in range(begin,lim):
    merge_sort_times2.append(time_sort(merge_sort, n))

plt.plot(x, merge_sort_times2, label="Merge Sort2", linestyle="--")

del merge_sort_times2
gc.collect()

merge_sort_times3 = []
for n in range(begin,lim):
    merge_sort_times3.append(time_sort(merge_sort, n))

plt.plot(x, merge_sort_times3, label="Merge Sort3", linestyle="-.")

plt.legend()
plt.show()