def find_first_invalid(num: list, preamble: int) -> int:
    for i in range(preamble, len(num)):
        possible = num[i - preamble : i]
        actual = num[i]
        valid = any([a + b == actual for a in possible for b in possible])
        if not valid:
            return actual


def find_summands(num: list, target: int) -> list:
    for i, a in enumerate(num):
        s = a
        for j, b in enumerate(num[i + 1 :]):
            s += b
            if s == target:
                return num[i : i + j + 2]


with open("input", "r") as f:
    num = [int(line) for line in f.readlines()]
    preamble = 25
    first = find_first_invalid(num, preamble)
    print(f"Part one: {first} is the first invalid number")

    summands = find_summands(num, first)
    print(max(summands) + min(summands))
