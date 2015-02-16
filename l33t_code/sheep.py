__author__ = 'abhishekanurag'

import math
import sys


def find_num_of_fields(farm):
    rows = len(farm)
    cols = len(farm[0])
    count = 0
    for i in xrange(rows):
        for j in xrange(cols):
            if farm[i][j] == "Y":
                if j - 1 < 0 or farm[i][j - 1] != "Y":
                    if i - 1 < 0 or farm[i - 1][j] != "Y":
                        count += 1
    return count


def find_count_of_even_sheep_arrangements(fields):
    if fields % 2 == 0:
        max_sheep = fields
    else:
        max_sheep = fields - 1
    max_arrangements = math.factorial(fields)
    arrangements = 1
    for sheep in xrange(2, max_sheep + 2, 2):
        cows = fields - sheep
        arrangements += (max_arrangements / (math.factorial(cows) * math.factorial(sheep)))
    return arrangements


def main():
    row_col = raw_input()
    row, col = map(int, row_col.split())
    farm = []
    for i in xrange(row):
        cols = raw_input()
        farm.append(list(cols))
    fields = find_num_of_fields(farm)
    arrangements = find_count_of_even_sheep_arrangements(fields)
    print arrangements % 1000000007

    print totalCellsVisited(9, 8)


def totalCellsVisited(n, m):
    grid = [[0] * m for i in xrange(n)]
    grid[0][0] = 1
    direction = "E"
    count = 1
    position = (0, 0)
    rights = 0
    while rights <= 4:
        new_x, new_y = cell_in_front(position, direction)
        if move_possible((new_x, new_y), n, m, grid):
            grid[new_x][new_y] = 1
            rights = 0
            direction = right_turn(direction)
            position = new_x, new_y
            count += 1
        else:
            rights += 1
            direction = right_turn(direction)
    return count


def move_possible(new_pos, n, m, grid):
    x, y = new_pos
    if 0 <= x < n and m > y >= 0 == grid[x][y]:
        return True
    else:
        return False


def cell_in_front(position, direction):
    x, y = position
    if direction == "E":
        return x, y + 1
    elif direction == "W":
        return x, y - 1
    elif direction == "N":
        return x - 1, y
    elif direction == "S":
        return x + 1, y


def right_turn(direction):
    if direction == "E":
        return "S"
    elif direction == "W":
        return "N"
    elif direction == "N":
        return "E"
    elif direction == "S":
        return "W"
    else:
        return None


if __name__ == "__main__":
    sys.exit(main())