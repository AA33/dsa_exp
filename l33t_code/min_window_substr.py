import sys

__author__ = 'abhishekanurag'


class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) == 0 or len(T) == 0:
            return ""
        chars = {}
        for ch in T:
            if ch in chars:
                chars[ch] += 1
            else:
                chars[ch] = 1
        to_be_seen = len(T)
        return self.minWindowHelp(S, chars, to_be_seen)

    def minWindowHelp(self, S, chars, to_be_seen):
        s_len = len(S)
        if s_len == 0:
            return ""
        ee = self.findInDirection(S, chars, True, to_be_seen, 0, s_len - 1)
        if ee == -1:
            return ""
        ls = self.findInDirection(S, chars, False, to_be_seen, 0, s_len - 1)

        if ls <= ee:
            ee_start = self.findInDirection(S, chars, False, to_be_seen, 0, ee)
            ls_end = self.findInDirection(S, chars, True, to_be_seen, ls, s_len - 1)
            if ls_end - ls < ee - ee_start:
                return S[ls:ls_end + 1]
            else:
                return S[ee_start:ee + 1]
        else:
            left = self.minWindowHelp(S[:ee + 1], chars, to_be_seen)
            right = self.minWindowHelp(S[ls:], chars, to_be_seen)
            middle = self.minWindowHelp(S[ee + 1:ls], chars, to_be_seen)
            left_len = len(left)
            mid_len = len(middle)
            right_len = len(right)
            char_len = len(chars)
            if left_len >= char_len and (mid_len == 0 or left_len <= mid_len) and (
                            right_len == 0 or left_len <= right_len):
                return left
            elif mid_len >= char_len and (left_len == 0 or mid_len <= left_len) and (
                            right_len == 0 or mid_len <= right_len):
                return middle
            else:
                return right

    # True = forward
    def findInDirection(self, S, letters, direction, to_be_seen, start, end):
        if direction:
            change = 1
            current = start
        else:
            change = -1
            current = end
        chars = letters.copy()
        seen = 0
        while start <= current <= end:
            s = S[current]
            if s in chars:
                if chars[s] > 0:
                    chars[s] -= 1
                    seen += 1
                    if seen == to_be_seen:
                        return current
            current += change
        return -1


def main():
    sol = Solution()
    print sol.minWindow("cabwefgewcwaefgcf", "cae")
    print sol.minWindow("acbbaca", "aba")
    print sol.minWindow("AB", "B")
    print sol.minWindow("A", "AA")
    print sol.minWindow("ADOBECODEBANC", "ABC")
    print sol.minWindow("AA", "AA")


if __name__ == "__main__":
    sys.exit(main())