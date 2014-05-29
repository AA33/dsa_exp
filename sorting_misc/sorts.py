__author__ = 'aanurag'

import sys

#Insertion sort
def less_than(a, b):
    if a < b:
        return True
    else:
        return False


def greater_than(a, b):
    if a != b and not less_than(a, b):
        return True
    else:
        return False


def insertion_sort(arr, order_func):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and not order_func(arr[i], key):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr


#Quicksort
def partition(arr, compare):
    i = -1
    if len(arr) > 0:
        i = 0
        part_elem = arr[i]
        for j in range(1, len(arr)):
            if compare(arr[j], part_elem):
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[0], arr[i] = arr[i], arr[0]
    return i


def quicksort(arr, compare=less_than):
    pivot_idx = partition(arr, compare)
    if pivot_idx == -1:
        #print('[]')
        return arr
    #print('Pivot=' + str(pivot_idx))
    #print(str(arr[:pivot_idx]) + str(arr[pivot_idx]) + str(arr[pivot_idx + 1:]))
    return quicksort(arr[:pivot_idx], compare) + [arr[pivot_idx]] + quicksort(arr[pivot_idx + 1:], compare)


#Montonic in 2D
def compare_gpa_sat(sat_and_gpa1, sat_and_gpa2):
    return sat_and_gpa1[0] < sat_and_gpa2[0]


def monotonic_in_2d(arr):
    longest_monotone = []
    running_monotone = []
    for i in range(len(arr)):
        if (len(running_monotone) == 0):
            running_monotone.append(arr[i])
            continue
        (last_sat, last_gpa) = running_monotone[-1]
        (sat, gpa) = arr[i]
        if (gpa < last_gpa):
            running_monotone.append((sat, gpa))
        elif (len(running_monotone) == 1):
            running_monotone = [(sat, gpa)]
        else:
            longest_monotone += running_monotone
            running_monotone = []
    return longest_monotone


#Main
def main():
    print("hello")
    a = [4, 3, 2, 1]
    #a = [1, 2, 3, 4]
    arr = [45, 18, 65, 3, 79, 79, 5, 4, 23, 81]
    print(len(a))
    print(insertion_sort(insertion_sort(a, less_than), less_than))
    print(quicksort(arr))

    #Monotonic2D
    #arr = [(0,0) for i in range(10)]
    arr = [(1500, 31), (1600, 32), (1700, 30), (1550, 40), (1560, 38), (1800, 33), (1900, 29), (2000, 28), (2100, 35)]
    print(quicksort(arr, compare_gpa_sat))
    print(monotonic_in_2d(quicksort(arr, compare_gpa_sat)))


if __name__ == "__main__":
    sys.exit(main())
