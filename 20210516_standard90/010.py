import sys


def _input():
    return sys.stdin.readline()


def main():
    num = int(_input().strip())

    c, p = [None] * num, [None] * num
    for i in range(num):
        line = _input().split(" ")
        c[i] = int(line[0])
        p[i] = int(line[1])

    sum1, sum2 = [0]*(num+1), [0]*(num+1)
    for i in range(num):
        sum1[i+1] = sum1[i]
        sum2[i+1] = sum2[i]
        if c[i] == 1:
            sum1[i+1] += p[i]
        if c[i] == 2:
            sum2[i+1] += p[i]

    num = int(_input().strip())
    for i in range(num):
        l, r = _input().split(" ")
        a1 = sum1[int(r)] - sum1[int(l)-1]
        a2 = sum2[int(r)] - sum2[int(l)-1]

        print(a1, a2)


if __name__ == '__main__':
    main()
