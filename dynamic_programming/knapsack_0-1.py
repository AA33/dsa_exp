__author__ = 'aanurag'

import sys
from lcs import printMemo

'''returns the maximum value of items that can be stolen
 items: list of tuples (value,weight); +ve ints
 max_weight: max weight allowed in your knapsack; +ve int
'''


def the_max_you_can_steal(items, max_weight):
    num_of_items = len(items)
    max_weight = int(max_weight)

    memo = []
    #fill memo with Nones and 0th row and column with 0s
    for i in range(num_of_items + 1):
        memo.append([] * (max_weight + 1))
        for j in range(max_weight + 1):
            if i == 0 or j == 0:
                memo[i].append(0)
            else:
                memo[i].append(None)
    included_items_prev = [[0]*(num_of_items+1)]*(max_weight+1)
    included_items_cur = [[0]*(num_of_items+1)]*(max_weight+1)
    #calculate memo values
    for item_num in range(1, num_of_items + 1):
        (cur_item_value, cur_item_wt) = items[item_num - 1]
        for weight in range(1, max_weight + 1):
            if cur_item_wt > weight:
                memo[item_num][weight] = memo[item_num - 1][weight]
            else:
                if memo[item_num - 1][weight] < memo[item_num - 1][weight - cur_item_wt] + cur_item_value:
                    memo[item_num][weight] = memo[item_num - 1][weight - cur_item_wt] + cur_item_value
                    included_items_cur[weight] = clone1DList(included_items_prev[weight-cur_item_wt])
                    included_items_cur[weight][item_num] = 1
                else:
                    memo[item_num][weight] = memo[item_num - 1][weight]
        included_items_prev = clone2DList(included_items_cur)

    print "Include items:"
    for i in range(len(included_items_cur[-1])):
        if included_items_cur[-1][i]==1:
            sys.stdout.write(str(i) + ', ')
    print
    return memo

def clone1DList(source):
    clone = [0]*len(source)
    for i in range(len(source)):
        clone[i] = source[i]
    return clone

def clone2DList(source):
    clone = []
    for i in range(len(source)):
        clone.append(clone1DList(source[i]))
    return clone


#Main
def main():
    print "Let's do some stealing!"
    items = [(84, 7), (16, 1), (7, 2), (10, 5)]
    sack_capacity = 9
    memo = the_max_you_can_steal(items, sack_capacity)
    print "Max value you can steal:" + str(memo[-1][-1])
    printMemo(memo)


if __name__ == "__main__":
    sys.exit(main())
