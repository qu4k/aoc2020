def find_two(numbers):
    for y in numbers:
        for x in numbers:
            if x + y == 2020:
                return [x, y]


def find_three(numbers):
    for z in numbers:
        for y in numbers:
            for x in numbers:
                if x + y + z == 2020:
                    return [x, y, z]


with open("input", "r") as f:
    numbers = [int(i) for i in f.readlines()]
    x1, y1 = find_two(numbers)
    print(f"Part one: {x1} * {y1} = {x1 * y1}")
    x2, y2, z2 = find_three(numbers)
    print(f"Part two: {x2} * {y2} * {z2} = {x2 * y2 * z2}")
