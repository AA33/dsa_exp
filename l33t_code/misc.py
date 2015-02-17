from collections import deque

__author__ = 'abhishekanurag'


def digits(n):
    if -9 <= n <= 9:
        return 1
    else:
        return 1 + digits(n / 10)


def powerset(s):
    powerset = ['']
    for ch in s:
        length = len(powerset)
        for i in range(length):
            powerset.append(powerset[i] + ch)
    return powerset


def words(code):
    keymap = {}
    keymap[2] = "abc"
    keymap[3] = "def"
    keymap[4] = "ghi"
    keymap[5] = "jkl"
    keymap[6] = "mno"
    keymap[7] = "pqrs"
    keymap[8] = "tuv"
    keymap[9] = "wxyz"

    words = list(keymap[int(code[0])])
    for num in code[1:]:
        letters = keymap[int(num)]
        length = len(words)
        for i in range(length):
            for letter in letters:
                words.append(words[i] + letter)
        words = words[length:]
    return words


def look_and_say(n):
    current = 1
    for _ in range(n):
        print current

        digit = current % 10
        current /= 10
        count = 1
        next_parts = []

        while current != 0:
            next_digit = current % 10
            if next_digit == digit:
                count += 1
            else:
                next_parts.append((digit, count))
                digit = next_digit
                count = 1
            current /= 10

        next_parts.append((digit, count))
        current = int(str(next_parts[-1][1]) + str(next_parts[-1][0]))

        for part in reversed(next_parts[:-1]):
            part_str = str(part[1]) + str(part[0])
            part_size = len(part_str)
            current *= (10 ** part_size)
            current += int(part_str)


def bfs(g, start):
    d = [False] * (len(g) + 1)
    p = [False] * (len(g) + 1)
    pts = [-1] * (len(g) + 1)
    d[start] = True
    q = deque()
    q.append(start)
    while len(q) > 0:
        v = q.popleft()
        print "Visited:" + str(v)
        # process_ve(v)
        nbors = g[v]
        for n in nbors:
            if not p[n]:
                # process_edge((v,n))
                print ((v, n))
            if not d[n]:
                d[n] = True
                pts[n] = v
                q.append(n)
        # process_vl(v)
        p[v] = True
    return pts


def dfs(g, start):
    d = [False] * (len(g) + 1)
    p = [False] * (len(g) + 1)
    pts = [-1] * (len(g) + 1)
    d[start] = True
    q = list()
    q.append(start)
    while len(q) > 0:
        v = q.pop()
        print "Visited:" + str(v)
        # process_ve(v)
        nbors = g[v]
        for n in reversed(nbors):
            if not p[n]:
                # process_edge((v,n))
                print ((v, n))
            if not d[n]:
                d[n] = True
                pts[n] = v
                q.append(n)
        # process_vl(v)
        p[v] = True
    return pts


g = {1: [2, 5, 6], 2: [1, 3, 5], 3: [2, 4], 4: [3, 5], 5: [1, 2, 4], 6: [1]}
wg = {0: [(1, 1), (3, 4), (4, 3)], 1: [(0, 1), (3, 3), (4, 2)], 2: [(5, 5), (4, 4)], 3: [(0, 4), (1, 4), (4, 4)],
      4: [(0, 3), (1, 2), (3, 4), (2, 4), (5, 7)], 5: [(4, 7), (2, 5)]}