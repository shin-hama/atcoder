import sys


def _input():
    return sys.stdin.readline()


def calc_common_divisor(a: int, b: int):
    if a == 0:
        return b
    elif b == 0:
        return a

    if a >= b:
        return calc_common_divisor(a % b, b)
    else:
        return calc_common_divisor(a, b % a)


def main():
    line = [int(n) for n in _input().split(" ")]

    common_a_b = calc_common_divisor(line[0], line[1])
    common_a_b_c = calc_common_divisor(common_a_b, line[2])
    result = sum([int(i // common_a_b_c) - 1 for i in line])

    print(result)


if __name__ == '__main__':
    main()
