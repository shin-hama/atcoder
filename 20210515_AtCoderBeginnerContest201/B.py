def parse_input(line):
    n, h = line.strip().split(" ")
    return {"name": n, "height": int(h)}


if __name__ == "__main__":
    num = int(input())
    args = [parse_input(line) for line in [input() for _ in range(0, num)]]
    result = sorted(args, key=lambda x: x["height"], reverse=True)
    print(result[1]["name"])
