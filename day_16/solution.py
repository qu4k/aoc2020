import re

from functools import reduce

re_field = re.compile(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)")


def parse_field(field: str) -> tuple:
    name, a, b, c, d = re_field.match(field).groups()
    a, b, c, d = [int(i) for i in [a, b, c, d]]
    return (name, (a, b), (c, d))


def inrange(v: int, r1: tuple, r2: tuple) -> bool:
    return r1[0] <= v <= r1[1] or r2[0] <= v <= r2[1]


with open("input", "r") as f:
    fields, my, samples = f.read().strip().split("\n\n")
    fields = [parse_field(field) for field in fields.split("\n")]
    my = [int(i) for i in my.split("\n")[1].split(",")]
    samples = [[int(i) for i in l.split(",")] for l in samples.split("\n")[1:]]

    invalid, valid = [[], []]
    for ticket in samples:
        vt = True
        for n in ticket:
            if not any(map(lambda r: inrange(n, r[1], r[2]), fields)):
                invalid.append(n)
                vt = False
        if vt:
            valid.append(ticket[:])

    print(f"Part one: {sum(invalid)} is the ticket scanning error rate")

    guesses = [fields[:] for _ in range(len(fields))]

    for ticket in valid:
        for i, n in enumerate(ticket):
            guesses[i] = list(filter(lambda r: inrange(n, r[1], r[2]), guesses[i]))

    guesses = [[y[0] for y in x] for x in guesses]
    order = [x[0] if len(x) == 1 else None for x in guesses]

    while any([len(x) != 1 for x in guesses]):
        for i in range(len(guesses)):
            if len(guesses[i]) > 1:
                guesses[i] = list(filter(lambda x: x not in order, guesses[i]))
        order = [x[0] if len(x) == 1 else None for x in guesses]

    vals = [my[i] for i, x in enumerate(order) if x.startswith("departure")]
    print(f"Part two: {reduce((lambda x, y: x * y), vals)} are `departure` values")
