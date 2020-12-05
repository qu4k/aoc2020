from functools import reduce
from operator import mul

with open("input", "r") as f:
    map = [line.strip() for line in f.readlines()]

    def get(pos):
        x, y = pos
        return map[y][x % len(map[0])]

    def count_trees(right, down):
        pos = (0, 0)
        trees = 0
        for _ in range(0, len(map) - 1, down):
            xx, yy = pos
            pos = (xx + right, yy + down)
            cell = get(pos)
            if cell == "#":
                trees += 1
        return trees

    one = count_trees(3, 1)
    print(f"Part one: {one} trees found")

    two = []
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        two.append(count_trees(right, down))
    two = reduce(mul, two)
    print(f"Part two: {two}")
