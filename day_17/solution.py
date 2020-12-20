from itertools import product

import numpy as np


def simulate(state: np.ndarray, directions: list, cycles: int) -> int:
    dim = len(np.shape(state))
    for _ in range(cycles):
        state = np.pad(state, [(1, 1) for _ in range(dim)], "constant")
        shape = np.shape(state)
        modif = np.copy(state)
        for coord in product(*[range(s) for s in shape]):
            active = 0
            for trasl in directions:
                trasl = tuple(n + mn for n, mn in zip(coord, trasl))
                if all(map(lambda x: 0 <= x[0] < x[1], zip(trasl, shape))):
                    if state[trasl]:
                        active += 1
            modif[coord] = 2 <= active <= 3 if state[coord] else active == 3
        state = modif
    return np.count_nonzero(state)


with open("input", "r") as f:
    lines = f.readlines()
    state = [[[0 if c == "." else 1 for c in line.strip()]] for line in lines]
    state = np.asarray(state, dtype=np.bool)

    directions = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
    directions.remove((0, 0, 0))

    print(f"Part one: {simulate(state, directions, 6)} active cubes")

    state = [[[[0] if c == "." else [1] for c in line.strip()]] for line in lines]
    state = np.asarray(state, dtype=np.bool)

    directions = list(product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1], [-1, 0, 1]))
    directions.remove((0, 0, 0, 0))

    print(f"Part one: {simulate(state, directions, 6)} active cubes")
