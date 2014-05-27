__author__ = 'aanurag'

import sys


def heapify(arr, size):
    i = 0
    while 1:
        left = 2 * i + 1
        right = left + 1

        if left < size and arr[left] < arr[i]:
            arr[left], arr[i] = arr[i], arr[left]
            sift_up(arr, i)
        if right < size and arr[right] < arr[i]:
            arr[right], arr[i] = arr[i], arr[right]
            sift_up(arr, i)
        if left == size or right == size:
            break
        i += 1


def sift_up(arr, i):
    if i == 0:
        return
    elif i % 2 == 0:
        parent = (i - 1) / 2
    else:
        parent = i / 2
    if arr[i] < arr[parent]:
        arr[i], arr[parent] = arr[parent], arr[i]
        sift_up(arr, parent)


def heapsort(arr):
    size = len(arr)
    while size > 0:
        heapify(arr, size)
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size -= 1
    return arr

#Main
def main():
    arr = [45, 18, 81, 65, 3, 79, 23, 5, 4, 78]
    print(heapsort(arr))


if __name__ == "__main__":
    sys.exit(main())