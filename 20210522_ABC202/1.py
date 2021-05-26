import sys


def _input():
    return sys.stdin.readline()[:]


def main():
    a, b, c = [int(i) for i in _input().strip().split(" ")]
    print(21 - (a + b + c))


if __name__ == "__main__":
    main()
