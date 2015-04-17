import math
import sys

__author__ = 'abhishekanurag'


def sudoko_verifier(solution):
    size = len(solution)

    for i in range(size):
        one_to_nine = set()
        for j in range(size):
            current = solution[i][j]
            if 0 < current < 10 and current not in one_to_nine:
                one_to_nine.add(current)
            else:
                return False

    for i in range(size):
        one_to_nine = set()
        for j in range(size):
            current = solution[j][i]
            if 0 < current < 10 and current not in one_to_nine:
                one_to_nine.add(current)
            else:
                return False

    increment = int(math.sqrt(size))
    row = 0
    column = 0

    while row < size and column < size:
        one_to_nine = set()
        for i in range(row, row + increment):
            for j in range(column, column + increment):
                current = solution[j][i]
                if 0 < current < 10 and current not in one_to_nine:
                    one_to_nine.add(current)
                else:
                    return False
        if row + increment < size:
            row += increment
        elif column + increment < size:
            row = 0
            column += increment
        else:
            break

    return True


def main():
    solution = [[2, 7, 6, 3, 1, 4, 9, 5, 8],
                [8, 5, 4, 9, 6, 2, 7, 1, 3],
                [9, 1, 3, 8, 7, 5, 2, 6, 4],
                [4, 6, 8, 1, 2, 7, 3, 9, 5],
                [5, 9, 7, 4, 3, 8, 6, 2, 1],
                [1, 3, 2, 5, 9, 6, 4, 8, 7],
                [3, 2, 5, 7, 8, 9, 1, 4, 6],
                [6, 4, 1, 2, 5, 3, 8, 7, 9],
                [7, 8, 9, 6, 4, 1, 5, 3, 2]]
    non_solution = [[2, 7, 6, 3, 1, 4, 9, 5, 8],
                    [8, 5, 4, 9, 6, 2, 7, 1, 3],
                    [9, 1, 3, 8, 7, 5, 2, 6, 4],
                    [4, 6, 8, 1, 2, 7, 3, 9, 5],
                    [5, 9, 7, 4, 3, 8, 6, 2, 1],
                    [1, 3, 2, 5, 9, 6, 4, 8, 7],
                    [3, 2, 5, 7, 8, 9, 1, 4, 6],
                    [6, 4, 1, 2, 5, 3, 8, 7, 9],
                    [7, 8, 9, 6, 4, 1, 5, 3, 3]]

    print sudoko_verifier(solution)
    print sudoko_verifier(non_solution)


if __name__ == '__main__':
    sys.exit(main())