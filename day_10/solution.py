import functools

from itertools import tee
from typing import Callable


def memoize(f: Callable) -> Callable:
    memo = {}

    @functools.wraps(f)
    def helper(x: int) -> int:
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


def pairwise(iterable: iter) -> iter:
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


with open("input", "r") as f:
    adapters = [int(line) for line in f.readlines()]
    adapters.sort()
    adapters.insert(0, 0)  # add the outlet
    adapters.append(adapters[-1] + 3)
    jumps = []
    for x, y in pairwise(adapters):
        jumps.append(y - x)
    print(jumps.count(1) * jumps.count(3))

    @memoize
    def explore(n: int) -> int:
        if n == len(adapters) - 1:
            return 1
        possibilities = 0
        start = adapters[n]
        for i, end in enumerate(adapters[n + 1 : n + 4]):
            if start >= end - 3:
                possibilities += explore(n + i + 1)
        return possibilities

    print(explore(0))
