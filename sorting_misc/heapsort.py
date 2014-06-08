__author__ = 'aanurag'

import sys
from sorts import less_than, greater_than


def heapify(arr, size=None, compare=greater_than):
    if not size:
        size = len(arr)
    i = 0
    while 1:
        left = 2 * i + 1
        right = left + 1

        if left < size and compare(arr[left], arr[i]):
            arr[left], arr[i] = arr[i], arr[left]
            sift_up(arr, i, compare)
        if right < size and compare(arr[right], arr[i]):
            arr[right], arr[i] = arr[i], arr[right]
            sift_up(arr, i, compare)
        if left >= size or right >= size:
            break
        i += 1


def sift_up(arr, i, compare):
    if i == 0:
        return
    elif i % 2 == 0:
        parent = (i - 1) / 2
    else:
        parent = i / 2
    if compare(arr[i], arr[parent]):
        arr[i], arr[parent] = arr[parent], arr[i]
        sift_up(arr, parent, compare)


def heapsort(arr):
    size = len(arr)
    while size > 0:
        heapify(arr, size)
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size -= 1
    return arr


def getMinMax(arr, compare=greater_than):
    minmax = None
    if len(arr) > 0:
        minmax = arr[0]
        arr[0] = arr[len(arr) - 1]
        arr.pop()
        heapify(arr,None,compare)
    return minmax


#Main
def main():
    arr = [45, 18, 81, 65, 3, 3, 79, 23, 5, 4, 78, 4, 5]
    heapify(arr)
    print(arr)
    getMinMax(arr)
    print(arr)
    print(heapsort(arr))
    print(heapsort([]))


if __name__ == "__main__":
    sys.exit(main())