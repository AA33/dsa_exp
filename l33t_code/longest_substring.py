import sys

__author__ = 'abhishekanurag'


def lengthOfLongestSubstring(s):
    if len(s) < 2:
        return len(s)
    max_length = 0
    seen = dict()
    start = 0
    end = start + 1
    seen[s[start]] = 0
    while end < len(s):
        if s[end] not in seen:
            seen[s[end]] = end
            end += 1
        else:
            length = end - start
            if length > max_length:
                max_length = length
            rep_pos = seen[s[end]]
            while start <= rep_pos:
                del seen[s[start]]
                start += 1
    length = end - start
    if length > max_length:
        max_length = length
    return max_length


def incr_decr_tuple(a):
    m = [(a[x], a[x + 1]) for x in range(0, len(a), 2)]
    rec_backtracker(m)
    z = []
    for t in m:
        z.append(t[0])
        z.append(t[1])
    return z


def rec_backtracker(a):
    if len(a) == 1 or len(a) == 0:
        return True
    all_good = False
    if check_order(a[0], a[1]):
        all_good = rec_backtracker(a[1:])
    else:
        a[1] = tuple_swap(a[1])
        if check_order(a[0], a[1]):
            all_good = rec_backtracker(a[1:])
    if not all_good:
        a[0] = tuple_swap(a[0])
        if check_order(a[0],a[1]):
            return rec_backtracker(a[1:])
        else:
            return False
    else:
        return True



def tuple_swap(b):
    return b[1], b[0]


def check_order(t1, t2):
    if t1[0] < t2[0] and t1[1] > t2[1]:
        return True
    else:
        return False


# Main
def main():
    s = "qopubjguxhxdipfzwswybgfylqvjzhar"
    print lengthOfLongestSubstring(s)
    num = [1, 5, 7, 1, 3, 8, 5, 6]
    print incr_decr_tuple(num)


if __name__ == "__main__":
    sys.exit(main())




