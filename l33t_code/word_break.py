import sys

__author__ = 'abhishekanurag'


class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        length = len(s)
        memo = [[None for i in range(length)] for j in range(length)]
        for i in range(length):
            for j in range(length):
                if i == j:
                    if s[i] in dict:
                        memo[i][i] = True
                    else:
                        memo[i][i] = False
                if j < i:
                    memo[i][j] = False
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                memo[i][j] = s[i:j + 1] in dict
                if not memo[i][j]:
                    for x in range(i, j + 1):
                        valid = memo[i][x] and memo[x+1][j]
                        memo[i][j] = memo[i][j] or valid
                        if memo[i][j]:
                            break
        return memo[0][length - 1]


# Main
def main():
    s = 'ab'
    dict = set()
    dict.add('a')
    dict.add('b')
    print Solution().wordBreak(s, dict)


if __name__ == "__main__":
    sys.exit(main())