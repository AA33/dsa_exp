# coding=utf-8

# Standard n queens problem.

"""
procedure bt(c,P)
  if reject(P,c) then return
  if accept(P,c) then output(P,c)
  s ← first(P,c)
  while s ≠ Λ do
    bt(s)
    s ← next(P,s)
"""
import sys
import itertools


def generate_cell(row, col):
    if row % 2 == 0:
        start_color = 'W'
    else:
        start_color = 'B'

    if col % 2 == 0:
        cell = start_color
    elif start_color == 'W':
        cell = 'B'
    else:
        cell = 'W'
    return cell, '-'


def problem(size):
    return [[generate_cell(i, j) for j in range(size)] for i in range(size)]


def print_board(prob):
    print "==============================================="
    for i in range(len(prob)):
        print ' '.join(map(lambda cell: cell[0] + cell[1], prob[i])) + '\n'
    print "==============================================="


def reject(sol):
    rows = [0 for _ in range(len(sol))]
    cols = list(rows)
    for i in range(len(sol)):
        for j in range(len(sol)):
            if sol[i][j][1] == 'Q':
                if rows[i] != 0 or cols[j] != 0 or not check_diagonals(sol, i, j):
                    return True
                else:
                    rows[i] += 1
                    cols[j] += 1
    return False


def accept(sol):
    if reject(sol):
        return False
    rows = [0 for _ in range(len(sol))]
    cols = list(rows)
    for i in range(len(sol)):
        for j in range(len(sol)):
            if sol[i][j][1] == 'Q':
                rows[i] += 1
                cols[j] += 1
    if sum(rows) == sum(cols) == len(sol):
        return True
    else:
        return False


def check_diagonals(sol, row, col):
    changes = [1, -1]
    for row_change, col_change in itertools.product(changes, changes):
        check_row = row + row_change
        check_col = col + col_change
        while 0 <= check_row < len(sol) and 0 <= check_col < len(sol):
            if sol[check_row][check_col][1] == 'Q':
                return False
            check_row += row_change
            check_col += col_change
    return True


def next_sol(sol):
    last_row = last_col = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            if sol[i][j][1] == 'Q':
                last_row = i
                last_col = j
    sol[last_row][last_col] = generate_cell(last_row, last_col)
    if last_col != len(sol) - 1:
        col = last_col + 1
        row = last_row
    else:
        return None
    sol[row][col] = sol[row][col][0], 'Q'
    return sol


def extend_sol(sol):
    last_row = -1
    for i in range(len(sol)):
        for j in range(len(sol)):
            if sol[i][j][1] == 'Q':
                last_row = i
    last_row += 1
    if last_row < len(sol):
        sol[last_row][0] = sol[last_row][0][0], 'Q'
        return sol
    else:
        return None


count = 0


def output(sol):
    global count
    count += 1
    print count
    print_board(sol)


def solver(prob):
    if reject(prob):
        return
    if accept(prob):
        output(prob)
    sol = extend_sol(prob)
    while sol:
        solver(sol)
        sol = next_sol(sol)


def main():
    global count

    count = 0
    prob = problem(8)
    print_board(prob)
    solver(prob)

    count = 0
    prob = problem(9)
    print_board(prob)
    solver(prob)


if __name__ == "__main__":
    sys.exit(main())