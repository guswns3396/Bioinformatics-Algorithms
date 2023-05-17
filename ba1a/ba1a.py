import sys


def PatternCount(txt, pat):
    count = 0
    for i in range(len(txt) - len(pat) + 1):
        if txt[i:i + len(pat)] == pat:
            count += 1
    return count


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        args = f.read().splitlines()
    print(PatternCount(args[0], args[1]))
