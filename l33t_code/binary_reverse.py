__author__ = 'abhishekanurag'
import sys


def get_reverse_binary_string(s):
    rev_binary = str(s & 1)
    while s > 1:
        s >>= 1
        rev_binary += str(s & 1)
    return rev_binary


def reverse_in_binary(n):
    rev_binary = get_reverse_binary_string(n)
    return int(rev_binary, 2)


def main():
    input_passed = False
    while not input_passed:
        try:
            n = raw_input("Enter an integer N\n")
            num = int(n)
            input_passed = True
        except ValueError:
            print "Please enter a valid integer."
    print reverse_in_binary(num)


if __name__ == "__main__":
    sys.exit(main())
