import re

policy = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")


def parse(line):
    m = policy.match(line)
    g = m.groups()
    return (int(g[0]), int(g[1]), g[2], g[3])


with open("input", "r") as f:
    checks = [parse(line) for line in f.readlines()]
    valid_one = []
    valid_two = []

    for low, high, c, psswd in checks:
        n = psswd.count(c)
        if low <= n <= high:
            valid_one.append(psswd)
        if bool(psswd[low - 1] == c) != bool(psswd[high - 1] == c):
            valid_two.append(psswd)

    print(f"Part one: {len(valid_one)} valid passwords")
    print(f"Part two: {len(valid_two)} valid passwords")
