def simulate(seq: list, end: int) -> int:
    known = {n: i for i, n in enumerate(seq)}
    for i in range(len(seq), end):
        last = seq[-1]
        if last in known and known[last] != i - 1:
            j = known[last]
            seq.append(i - 1 - j)
        else:
            seq.append(0)
        known[last] = i - 1
    return seq[-1]


with open("input", "r") as f:
    nums = [int(i) for i in f.read().split(",")]
    print(f"Part one: {simulate(nums[::], 2020)} is the 2020th #")
    print(f"Part two: {simulate(nums[::], 30000000)} is the 30000000th #")
