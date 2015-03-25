__author__ = 'abhishekanurag'

arr1 = [1]
arr2 = [1, 2]
arr3 = [1, 2, 3]
arr11 = [1, 1, 1]
arr112 = [1, 1, 2]
arrx = [23, 45, 67, 67, 77, 77, 77, 77, 77, 81, 81]


def search(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] < x:
            start = mid + 1
        elif arr[mid] > x:
            end = mid - 1
        else:
            return mid
    return -(start + 1)


def search_first(arr, x):
    start = 0
    end = len(arr) - 1
    first = float('-inf')
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == x:
            first = mid
            end = mid - 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    if first != float('-inf'):
        return first
    return -(start + 1)


def search_last(arr, x):
    start = 0
    end = len(arr) - 1
    last = float('inf')
    while start <= end:
        mid = (start + end) / 2
        if arr[mid] == x:
            last = mid
            start = mid + 1
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    if last != float('inf'):
        return last
    return -(start + 1)