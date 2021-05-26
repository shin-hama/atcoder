import sys


def _input():
    return sys.stdin.readline()[:]


def main():
    dataset = {
        "0": "0",
        "1": "1",
        "6": "9",
        "8": "8",
        "9": "6",
    }

    result = "".join([dataset[k] for k in reversed(_input().strip())])
    print(result)


if __name__ == '__main__':
    main()
