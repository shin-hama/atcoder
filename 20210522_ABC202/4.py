import sys


def _input():
    return sys.stdin.readline()


def gen_str(s: str, k):
    for _ in range(k - 1):
        if s[-1] == "a":
            min_b = s.rfind("b")
            a_min_i = s[:min_b].rfind("a")
            front = s[:a_min_i] if s[:a_min_i] else ""
            bb = s[a_min_i+1:min_b] if s[a_min_i+1:min_b] else ""
            end = s[min_b+1:] if s[min_b+1:] else ""
            s = f"{front}ba{end}{bb}"
        else:
            a_min_i = s.rfind("a")
            front = s[:a_min_i] if s[:a_min_i] else ""
            end = s[a_min_i+2:] if s[a_min_i+2:] else ""
            s = f"{front}ba{end}"

        yield s


def main():
    a, b, k = [int(i) for i in _input().strip().split(" ")]
    s = (f'{"a"*a}{"b"*b}')

    if k <= 1:
        print(s)
        return
    print([i for i in gen_str(s, k)][-1])


if __name__ == '__main__':
    main()
