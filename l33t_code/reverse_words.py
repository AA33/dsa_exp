import sys

__author__ = 'abhishekanurag'


def reverseWords(s):
    s = s.strip()
    x = s.split(' ')
    x = x[::-1]
    i = 0
    while 1:
        if i == len(x):
            break
        if x[i] == '':
            x.pop(i)
        else:
            i += 1
    return ' '.join(x)


# Main
def main():
    s = "   a    b "
    print reverseWords(s)


if __name__ == "__main__":
    sys.exit(main())