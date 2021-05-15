import math
from collections import defaultdict


if __name__ == "__main__":
    line = input()

    val = defaultdict(int)
    for c in line:
        val[c] += 1

    if val["o"] > 4 or val["x"] == 10:
        print(0)
        exit()

    result = math.factorial(val["o"])

    missing = 4 - val["o"]
    if missing != 0:
        maru_case =
        hatena_case = result * (3 ^ val["?"]) * ()
        result = maru_case + hatena_case
    print(result)
