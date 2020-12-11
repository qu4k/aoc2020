import copy

N, F, O = (None, 0, 1)
W, H = (0, 0)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def sim_1(grid: list) -> (list, bool):
    frame = [row[:] for row in grid]
    changed = False
    for y in range(H):
        for x in range(W):
            occ = 0
            for mx, my in directions:
                if 0 <= x + mx < W and 0 <= y + my < H:
                    if grid[y + my][x + mx] == O:
                        occ += 1
            if grid[y][x] == F and occ == 0:
                frame[y][x] = O
                changed = True
            elif grid[y][x] == O and occ >= 4:
                frame[y][x] = F
                changed = True
    return (frame, changed)


def sim_2(grid: list) -> (list, bool):
    frame = [row[:] for row in grid]
    changed = False
    for y in range(H):
        for x in range(W):
            occ = 0
            for mx, my in directions:
                xx = x
                yy = y
                while 0 <= xx + mx < W and 0 <= yy + my < H:
                    xx += mx
                    yy += my
                    if grid[yy][xx] == O:
                        occ += 1
                    if grid[yy][xx] != N:
                        break
            if grid[y][x] == F and occ == 0:
                frame[y][x] = O
                changed = True
            elif grid[y][x] == O and occ >= 5:
                frame[y][x] = F
                changed = True
    return (frame, changed)


with open("input", "r") as f:
    grid = [
        [N if char == "." else (F if char == "L" else O) for char in list(line.strip())]
        for line in f.readlines()
    ]
    W, H = (len(grid[0]), len(grid))

    frame = [row[:] for row in grid]
    changed = True
    while changed:
        frame, changed = sim_1(frame)

    print(sum(row.count(O) for row in frame))

    frame = [row[:] for row in grid]
    changed = True
    while changed:
        frame, changed = sim_2(frame)

    print(sum(row.count(O) for row in frame))
