__author__ = 'aanurag'

from sorts import *
import random

#T=O(n)
def kth_smallest(arr, k):
    if k >= len(arr) or k < 0:
        return None
    #pivot_idx = partition(arr)
    pivot_idx = randomized_partition(arr)
    if pivot_idx == k:
        return arr[k]
    elif pivot_idx < k:
        return kth_smallest(arr[pivot_idx + 1:], k - pivot_idx - 1)
    else:
        return kth_smallest(arr[:pivot_idx], k)


#T=O(n)
def kth_largest(arr, k):
    return kth_smallest(arr, len(arr) - k - 1)


#T=O(n)
def randomized_partition(arr):
    rand = random.randrange(len(arr))
    arr[0], arr[rand] = arr[rand], arr[0]
    return partition(arr)


#Main
def main():
    arr = [18, 45, 65, 3, 79, 5, 4, 23, 81]

    print(kth_smallest(arr, 5))
    print(kth_largest(arr, 3))


if __name__ == "__main__":
    sys.exit(main())