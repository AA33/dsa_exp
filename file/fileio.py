import os
import sys

__author__ = 'abhishekanurag'


def main():
    f = open("file.txt", 'r')
    line = f.readline()
    parts = [int(p) for p in line.split(' ')]
    matrix = []
    for i in range(1, parts[0] + 1):
        line = f.readline()
        matrix.append([int(x) for x in line.split(' ')])
    print matrix

    f.close()
    print os.getcwd()
    os.chdir('../')
    print os.getcwd()
    pass


if __name__ == "__main__":
    sys.exit(main())