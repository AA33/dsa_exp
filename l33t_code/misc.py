from collections import deque
from heapq import heapify, heappop, heappush
import itertools
import sys

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
    keymap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

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


def permutations(s):
    if len(s) == 0:
        return ['']
    ch = s[0]
    smaller_perms = permutations(s[1:])
    print smaller_perms
    perms = []
    for perm in smaller_perms:
        for i in range(len(perm) + 1):
            nperm = perm[:i] + ch + perm[i:]
            print nperm
            perms.append(nperm)
    return perms


def permutations2(s):
    if len(s) == 0:
        return ['']
    chars = ''.join(sorted(s))
    perms = [chars]
    last_perm = False
    cur = list(chars)
    while not last_perm:
        i = len(cur) - 2
        # From end find first place that is still ordered
        while i >= 0:
            if ord(cur[i]) < ord(cur[i + 1]):
                break
            i -= 1
        if i < 0:
            last_perm = True
            continue
        j = len(cur) - 1
        # From end find first that can reverse the order
        while j > i:
            if ord(cur[i]) < ord(cur[j]):
                break
            j -= 1
        # Swap
        cur[i], cur[j] = cur[j], cur[i]
        # Reverse after the swap
        cur = cur[:i + 1] + list(reversed(cur[i + 1:]))
        perms.append(''.join(cur))
    print len(perms)
    return perms


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

INFINITY = 99999
REMOVED = -1
counter = itertools.count()


def push(heap, finder, item, weight):
    if item in finder:
        remove(item, finder)
    entry = [weight, item]
    finder[item] = entry
    heappush(heap, entry)


def remove(item, finder):
    entry = finder.pop(item)
    entry[-1] = REMOVED


def pop(heap, finder):
    while len(heap) > 0:
        weight, item = heappop(heap)
        if item != REMOVED:
            del finder[item]
            return item, weight
    raise KeyError("No more items")


def dijkstra(graph, source):
    # Initialize distance, visited and path arrays
    finder = {}
    distance = []
    final_distances = [INFINITY for _ in graph]
    for vertex in graph:
        if vertex != source:
            push(distance, finder, vertex, INFINITY)
    push(distance, finder, source, 0)
    final_distances[source] = 0
    previous = [-1] * len(graph)

    # While there are unvisited vertices
    while len(finder) > 0:
        # Find and remove the one with the lowest distance
        vertex, vertex_distance = pop(distance, finder)
        # For all it's neighbors
        neighbors = graph[vertex]
        for (neighbor, edge_weight) in neighbors:
            # If their nearest hasn't been found
            if neighbor in finder:
                current_distance, _ = finder[neighbor]
                # Update weight if path through this vertex is shorter
                alternate_distance = vertex_distance + edge_weight
                if alternate_distance < current_distance:
                    push(distance, finder, neighbor, alternate_distance)
                    final_distances[neighbor] = alternate_distance
                    previous[neighbor] = vertex
    print previous
    print final_distances


def prim(graph, source):
    tree = []
    visited = set()
    visited.add(source)
    possible_edges = []
    for neighbor, distance in graph[source]:
        heappush(possible_edges, (distance, source, neighbor))
    while len(tree) < len(graph) - 1:
        _, v1, v2 = heappop(possible_edges)
        if v1 in visited and v2 not in visited:
            tree.append((v1, v2))
            visited.add(v2)
            for neighbor, distance in graph[v2]:
                heappush(possible_edges, (distance, v2, neighbor))
    print tree


def contract_edge(graph, v1, v2):
    # Remove edge from both vertices
    graph[v1] = [(n, w) for (n, w) in graph[v1] if n != v2]
    print graph
    graph[v2] = [(n, w) for (n, w) in graph[v2] if n != v1]
    # Update v2's neighbors
    for neighbor, _ in graph[v2]:
        graph[neighbor] = [(n, w) for (n, w) in graph[neighbor] if n != v1]
        for index, (neighbors_neighbor, wt) in enumerate(graph[neighbor]):
            if neighbors_neighbor == v2:
                graph[neighbor][index] = v1, wt
    print graph
    # Copy over edges from v2 to v1
    graph[v1].extend(graph[v2])
    print graph
    # Delete v2
    del graph[v2]
    print graph
    return graph


def levenshtein(s1, s2):
    levs = [[-1 for _ in range(len(s1))] for _ in range(len(s2))]
    for i in range(len(s1)):
        levs[0][i] = i
    for j in range(len(s2)):
        levs[j][0] = j

    for j in range(1, len(s1)):
        for i in range(1, len(s2)):
            if s1[j] == s2[i]:
                work = levs[i - 1][j - 1]
            else:
                work = min(levs[i][j - 1], levs[i - 1][j], levs[i - 1][j - 1]) + 1
            levs[i][j] = work
    print levs


def strip_brackets(s):
    if s[0] == '(' and s[-1] == ')':
        return strip_brackets(s[1:-1])
    else:
        return s


def expand(s):
    s = strip_brackets(s)
    return expand_help(s)


def expand_help(s):
    if len(s) == 0:
        return []
    exp = []
    alpha = ''
    i = 0
    while i < len(s):
        ch = s[i]
        if ch == '(':
            j = find_closer(s, i)
            new = expand_help(s[i + 1:j])
            i = j
            if alpha != '':
                new = [alpha + part for part in new]
                alpha = ''
            if len(exp) > 0 and type(exp[-1]) is type(list()):
                last = exp.pop()
                exp.append([part1 + part2 for part1 in last for part2 in new])
            else:
                exp.append(new)
        elif ch.isalpha():
            alpha += ch
        elif ch == ',':
            if len(exp) > 0 and type(exp[-1]) is type(list()):
                exp[-1] = [part + alpha for part in exp[-1]]
                last = exp.pop()
                exp.extend(last)
            elif alpha != '':
                exp.append(alpha)
            alpha = ''
        i += 1
    if len(exp) > 0 and type(exp[-1]) is type(list()):
        exp[-1] = [part + alpha for part in exp[-1]]
        last = exp.pop()
        exp.extend(last)
    elif alpha != '':
        exp.append(alpha)
    return exp


def find_closer(s, i):
    opens = 1
    closes = 0
    k = i + 1
    while opens != closes:
        if s[k] == '(':
            opens += 1
        elif s[k] == ')':
            closes += 1
        k += 1
    return k - 1


def main():
    print expand("m(v,b)")
    print expand("(v,b)m")
    print expand("(v,b)mo")
    print expand("a(v,b)m")
    print expand("a(v,b)m(x,y),p,q,r,(x)s(e,o)")

    arr1 = [1]
    arr2 = [1,2]
    arr3 = [1,2,3]
    arr11 = [1,1]
    arr112 = [1,1,2]

    dijkstra(wg, 0)
    prim(wg, 0)
    contract_edge(wg, 0, 1)
    levenshtein("Saturday", "Sunday")


if __name__ == "__main__":
    sys.exit(main())


