def parse(chars: list):
    rows = (0, 127)
    cols = (0, 7)
    for step in chars[:7]:
        half = (rows[1] - rows[0]) // 2
        if step == "F":
            rows = (rows[0], rows[0] + half)
        else:
            rows = (rows[1] - half, rows[1])
    for step in chars[7:]:
        half = (cols[1] - cols[0]) // 2
        if step == "L":
            cols = (cols[0], cols[0] + half)
        else:
            cols = (cols[1] - half, cols[1])
    return ("".join(chars), rows[0], cols[0])


def id(seat: tuple):
    return seat[1] * 8 + seat[2]


with open("input", "r") as f:
    seats = [parse(list(line.strip())) for line in f.readlines()]
    seat_ids = [id(seat) for seat in seats]

    print(f"Part one: {max(seat_ids)} highest seat ID")

    diff = list(set(list(range(49, 807))) - set(seat_ids))
    print(f"Part one: {diff[0]} personal seat ID")
