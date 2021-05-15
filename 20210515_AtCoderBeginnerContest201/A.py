def parse_input(text):
    return [int(s) for s in text.strip().split(" ")]


if __name__ == "__main__":
    s = input()
    args = parse_input(s)
    array = sorted(args)

    pre_diff = None
    for i, j in zip(array, array[1:]):
        diff = j - i
        if pre_diff == diff:
            continue
        elif pre_diff is None:
            pre_diff = diff
        else:
            result = "No"
            break
    else:
        result = "Yes"

    print(result)
