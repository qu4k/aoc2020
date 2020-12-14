import re
import itertools

re_mask = re.compile(r"mask = ([0-9X]+)")
re_edit = re.compile(r"mem\[(\d+)\] = (\d+)")

N = 36


def bitarray(arr: list) -> int:
    return sum([b << i for i, b in enumerate(arr[::-1])])


def clean_mask(mask: str) -> list:
    return [int(i) if i != "X" else "X" for i in mask]


def exec_mask_1(mask: list, val: int) -> int:
    val = [val >> i & 1 for i in range(N - 1, -1, -1)]
    val = [m if m != "X" else v for v, m in zip(val, mask)]
    return bitarray(val)


def execute_1(lines: list) -> dict:
    mask = ""
    mem = {}
    for line in lines:
        match = re_mask.match(line)
        if match:
            mask = clean_mask(match.group(1))
            continue
        match = re_edit.match(line)
        addr, val = match.groups()
        mem[int(addr)] = exec_mask_1(mask, int(val))
    return mem


def exec_mask_2(mask: list, addr: int) -> list:
    addr = [addr >> i & 1 for i in range(N - 1, -1, -1)]
    addr = [
        [0, 1] if m == "X" else ([1] if m == 1 else [a]) for a, m in zip(addr, mask)
    ]
    return [bitarray(a) for a in list(itertools.product(*addr))]


def execute_2(lines: list) -> dict:
    mask = ""
    mem = {}
    for line in lines:
        match = re_mask.match(line)
        if match:
            mask = clean_mask(match.group(1))
            continue
        match = re_edit.match(line)
        addr, val = match.groups()
        for addr in exec_mask_2(mask, int(addr)):
            mem[int(addr)] = int(val)
    return mem


with open("input", "r") as f:
    lines = f.readlines()
    print(f"Part one: {sum(execute_1(lines).values())} mem")
    print(f"Part two: {sum(execute_2(lines).values())} mem")
