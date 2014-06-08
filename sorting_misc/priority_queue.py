import sys
from sorting_misc.sorts import less_than, greater_than

__author__ = 'aanurag'


class PriorityQueueElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class PriorityQueue:
    def __init__(self, minOrMax):
        if minOrMax == 'min':
            self.compare = less_than
        else:  #max or anything else
            self.compare = greater_than
        self.priorityArray = []

    def __str__(self):
        opt = '['
        for elem in self.priorityArray:
            opt += (str(elem) + ', ')
        opt += ']'
        return opt

    def addPriorityQueueElement(self, elem):
        self.priorityArray.append(elem)

    def getMaxOrMin(self):
        return self.priorityArray[0]

    def deleteMaxOrMin(self):
        minmax = None
        arr = self.priorityArray
        if len(arr) > 0:
            minmax = arr[0]
            arr[0] = arr[len(arr) - 1]
            arr.pop()
        return minmax

    def heapify(self, size=None):
        if not size:
            size = len(self.priorityArray)
        i = 0
        arr = self.priorityArray
        while 1:
            left = 2 * i + 1
            right = left + 1

            if left < size and self.compare(arr[left].key, arr[i].key):
                arr[left], arr[i] = arr[i], arr[left]
                self._sift_up(i)
            if right < size and self.compare(arr[right].key, arr[i].key):
                arr[right], arr[i] = arr[i], arr[right]
                self._sift_up(i)
            if left >= size or right >= size:
                break
            i += 1

    def _sift_up(self, i):
        if i == 0:
            return
        elif i % 2 == 0:
            parent = (i - 1) / 2
        else:
            parent = i / 2
        arr = self.priorityArray
        if self.compare(arr[i].key, arr[parent].key):
            arr[i], arr[parent] = arr[parent], arr[i]
            self._sift_up(parent)

    def empty(self):
        if len(self.priorityArray) > 0:
            return False
        else:
            return True

    def findPriority(self,value):
        for elem in self.priorityArray:
            if elem.value == value:
                return elem.key
        return None

    def setPriority(self,value,key):
        for elem in self.priorityArray:
            if elem.value == value:
                elem.key = key


#Main
def main():
    arr = [45, 18, 81, 65, 3, 79, 23, 78, 4, 5]
    PRQ = PriorityQueue('min')
    for i in range(len(arr)):
        elem = PriorityQueueElement(arr[i], 'ABC')
        PRQ.addPriorityQueueElement(elem)
    PRQ.heapify()
    print(PRQ)
    print(PRQ.getMaxOrMin())
    PRQ.deleteMaxOrMin()
    PRQ.heapify()
    print(PRQ.getMaxOrMin())


if __name__ == "__main__":
    sys.exit(main())