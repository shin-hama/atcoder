from collections import defaultdict
import sys


def _input():
    return sys.stdin.readline()


def main():
    _ = int(_input())
    abc = [None] * 3
    for i in range(3):
        abc[i] = [int(i) for i in _input().strip().split(" ")]

    b = abc[1]
    b = [b[i-1] for i in abc[2]]

    b_element = defaultdict(int)
    for i in b:
        b_element[i] += 1

    print(sum([b_element[j] for j in abc[0]]))


if __name__ == '__main__':
    main()
