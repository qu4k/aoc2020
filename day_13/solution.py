from functools import reduce


def crt(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def repeat(t: int, target: int) -> tuple:
    rep = t
    while rep < target:
        rep += t
    return (t, rep)


with open("input", "r") as f:
    lines = f.readlines()
    earliest = int(lines[0])

    pattern = [int(n) if n != "x" else None for n in lines[1].split(",")]
    buses = [bus for bus in pattern if bus != None]

    bus, time = min([repeat(bus, earliest) for bus in buses], key=lambda a: a[1])
    print(bus * (time - earliest))

    n, a = zip(*[(n, -a) for a, n in enumerate(pattern) if n != None])
    print(crt(n, a))
