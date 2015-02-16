import sys
import itertools

__author__ = 'abhishekanurag'

# KMP String matching algorithm

'''
KMP Table is built such that:
T[i] = Longest proper prefix of P[0...i] which is also a proper suffix of P[0...i]
If there is no such prefix T[i] = 0

Proper prefix: Prefix with length > 0
Proper suffix: Suffix with length > 0
'''


def build_kmp_table(pattern):
    T = [0] * len(pattern)
    p = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[p]:
            T[i] = p + 1  # length so index+1
            p += 1
        else:
            # T[i] = 0 anyway
            p = 0
        i += 1
    return T


def find(pattern, text):
    if len(pattern) == 0 or len(text) == 0:
        return -1
    p = t = 0
    T = build_kmp_table(pattern)
    while p + t < len(text):
        if pattern[p] == text[t + p]:
            if p == len(pattern) - 1:
                return t
            p += 1
        elif p > 0 and T[p - 1] > 0:
            t = t + p - T[p-1]
            p = T[p - 1]
        else:
            t = t + p + 1
            p = 0

    return -1


def main():
    print build_kmp_table("ABCDABD")
    print list(zip(range(0, 100), build_kmp_table("PARTICIPATE IN PARACHUTE")))
    print "Base cases:"
    print find('ABCD', '') == -1
    print find('', '') == -1
    print find('', 'CDE') == -1

    print "Small cases:"
    print find('A', 'BAC') == 1
    print find('A', 'ACB') == 0
    print find('AB', 'BCFGABCDEF') == 4
    print find('ABCDE', 'BCFGABCDEF') == 4
    print find('XX', 'BCFGABCDEF') == -1

    print "Larger cases:"
    print find("ABCDABD", "ABC ABCDAB ABCDABCDABDE") == 15
    print find("love", "This letter of love from me to you.") == 15
    print find("love", "This letter of lo lov love from me to you.") == 22
    print find("love", "This love letter from me to you.") == 5
    print find("hate", "This unloved letter from me to you.") == -1


if __name__ == "__main__":
    sys.exit(main())
    





