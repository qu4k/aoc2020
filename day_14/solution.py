import re

from itertools import product

re_mask = re.compile(r"mask = ([0-9X]+)")
re_edit = re.compile(r"mem\[(\d+)\] = (\d+)")

N = 36


def bitarray(arr: list) -> int:
    return sum([b << i for i, b in enumerate(arr[::-1])])


def clean_mask(mask: str) -> list:
    return [int(i) if i != "X" else "X" for i in mask]


def mask_val(mask: list, val: int) -> int:
    val = [val >> i & 1 for i in range(N - 1, -1, -1)]
    val = [m if m != "X" else v for v, m in zip(val, mask)]
    return bitarray(val)


def mask_addr(mask: list, addr: int) -> list:
    addr = [addr >> i & 1 for i in range(N - 1, -1, -1)]
    addr = [
        [0, 1] if m == "X" else ([1] if m == 1 else [a]) for a, m in zip(addr, mask)
    ]
    return [bitarray(a) for a in list(product(*addr))]


def execute(lines: list, edit_addr=False, edit_val=False) -> dict:
    mask = ""
    mem = {}
    for line in lines:
        match = re_mask.match(line)
        if match:
            mask = clean_mask(match.group(1))
            continue
        match = re_edit.match(line)
        addr, val = (int(i) for i in match.groups())
        if edit_val:
            val = mask_val(mask, val)
        if edit_addr:
            for addr in mask_addr(mask, addr):
                mem[addr] = val
        else:
            mem[addr] = val
    return mem


with open("input", "r") as f:
    lines = f.readlines()
    print(f"Part one: {sum(execute(lines, edit_val=True).values())} mem")
    print(f"Part two: {sum(execute(lines, edit_addr=True).values())} mem")
