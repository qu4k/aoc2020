import re
from math import sin, cos, radians

dirs = ["N", "E", "S", "W"]
re_action = re.compile(r"(N|S|E|W|L|R|F)(\d+)")


def parse(action: str) -> tuple:
    direction, amount = re_action.match(action).groups()
    return (direction, int(amount))


def try_move(x, y, direction, amount) -> tuple:
    if direction == "N":
        y += amount
    elif direction == "S":
        y -= amount
    elif direction == "E":
        x += amount
    elif direction == "W":
        x -= amount
    return (x, y)


def try_rotate(current: str, amount: int) -> str:
    i = dirs.index(current)
    return dirs[(i + int(amount / 90)) % len(dirs)]


def move_ship(actions: list) -> tuple:
    pos = (0, 0)
    current = "E"
    for (direction, amount) in actions:
        if direction == "L":
            current = try_rotate(current, amount)
        elif direction == "R":
            current = try_rotate(current, amount)
        elif direction == "F":
            pos = try_move(*pos, current, amount)
        else:
            pos = try_move(*pos, direction, amount)
    return pos


def try_rotate_waypoint(x: int, y: int, amount: int) -> tuple:
    th = radians(amount)
    return (round(x * cos(th) - y * sin(th)), round(x * sin(th) + y * cos(th)))


def move_by_waypoint(actions: list) -> tuple:
    pos = (0, 0)
    waypoint = (10, 1)
    for (direction, amount) in actions:
        if direction == "L":
            waypoint = try_rotate_waypoint(*waypoint, amount)
        elif direction == "R":
            waypoint = try_rotate_waypoint(*waypoint, -amount)
        elif direction == "F":
            pos = tuple([p + amount * c for p, c in zip(pos, waypoint)])
        else:
            waypoint = try_move(*waypoint, direction, amount)
        print(direction, amount, waypoint, pos)
    return pos


with open("input", "r") as f:
    actions = [parse(line) for line in f.readlines()]
    x, y = move_ship(actions)
    print(f"Part one: {abs(x) + abs(y)} Manhattan distance")
    x, y = move_by_waypoint(actions)
    print(f"Part two: {abs(x) + abs(y)} Manhattan distance")
