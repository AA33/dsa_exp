__author__ = 'aanurag'

import sys


def memoizeSolution(seq1, seq2):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)
    memo = []
    #fill memo with Nones and 0th row and column with 0s
    for i in range(len_seq1 + 1):
        memo.append([] * (len_seq2 + 1))
        for j in range(len_seq2 + 1):
            if i == 0 or j == 0:
                memo[i].append(0)
            else:
                memo[i].append(None)
    #calculate memos
    for i in range(1, len_seq1 + 1):
        for j in range(1, len_seq2 + 1):
            if not memo[i][j]:
                if seq1[i - 1] == seq2[j - 1]:
                    memo[i][j] = memo[i - 1][j - 1] + 1
                else:
                    if memo[i - 1][j] >= memo[i][j - 1]:
                        memo[i][j] = memo[i - 1][j]
                    else:
                        memo[i][j] = memo[i][j - 1]
    return memo


def printOneLongestCommonSubsequence(str1, str2):
    memo = memoizeSolution(str1, str2)
    i = len(memo) - 1
    j = len(memo[0]) - 1
    LCS = ''
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            LCS = LCS + str1[i - 1]
            i -= 1
            j -= 1
        else:
            if memo[i][j - 1] > memo[i - 1][j]:
                j -= 1
            else:
                i -= 1
    print LCS[::-1]


def printAllLongestCommonSubsequences(str1, str2, memo=None, i=None, j=None, solutionSet=None, willPrint=True):
    if not memo:
        memo = memoizeSolution(str1, str2)
    if not i:
        i = len(memo) - 1
    if not j:
        j = len(memo[0]) - 1
    if not solutionSet:
        solutionSet = []

    if str1[i - 1] == str2[j - 1]:
        printAllLongestCommonSubsequences(str1, str2, memo, i - 1, j - 1, solutionSet, False)
        for s in solutionSet:
            s = s + str1[i - 1]
    else:
        if memo[i - 1][j] >= memo[i][j]:
            printAllLongestCommonSubsequences(str1, str2, memo, i - 1, j, solutionSet, False)
        if memo[i][j - 1] >= memo[i][j]:
            ex_sol = []
            printAllLongestCommonSubsequences(str1, str2, memo, i, j - 1, ex_sol, False)
            for s in ex_sol:
                solutionSet.append(s)

    if willPrint:
        for s in solutionSet:
            print s[::-1]


def printMemo(memo):
    rows = len(memo)
    columns = len(memo[0])
    for i in range(columns):
        for j in range(rows):
            sys.stdout.write(str(memo[j][i]) + ' ')
        print


#Main
def main():
    memo = memoizeSolution('ABCBDAB', 'BDCABA')
    printMemo(memo)
    # printCommonSequences('ABCBDAB', 'BDCABA')
    printOneLongestCommonSubsequence('ABCBDAB', 'BDCABA')
    # printAllLongestCommonSubsequences('ABCBDAB','BDCABA')


if __name__ == "__main__":
    sys.exit(main())