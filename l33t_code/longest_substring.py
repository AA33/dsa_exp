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

# Main
def main():
    s = "qopubjguxhxdipfzwswybgfylqvjzhar"
    print lengthOfLongestSubstring(s)


if __name__ == "__main__":
    sys.exit(main())




