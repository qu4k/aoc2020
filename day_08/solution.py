import re

re_op = re.compile(r"([a-z]{3}) ([+-]\d+)")


def parse(op: str) -> tuple:
    op, arg = re_op.match(op).groups()
    return (op, int(arg))


def execute(inst) -> int:
    ran = []
    acc = 0
    ip = 0

    while True:
        if ip in ran or not len(inst) - 1 > ip:
            return (acc, not len(inst) - 1 > ip)
        op, arg = inst[ip]
        ran.append(ip)
        if op == "acc":
            acc += arg
            ip += 1
        elif op == "jmp":
            ip += arg
        elif op == "nop":
            ip += 1


def change_op(to: str, i: int, inst: list) -> list:
    inst_c = inst.copy()
    inst_c[i] = (to, inst_c[i][1])
    return inst_c


with open("input", "r") as f:
    inst = [parse(line) for line in f.readlines()]
    acc, _ = execute(inst)

    print(f"Part one: acc={acc} before loop")

    jmps = [i for i, (name, _) in enumerate(inst) if name == "jmp"]
    nops = [i for i, (name, _) in enumerate(inst) if name == "nop"]

    jmps = [execute(change_op("nop", i, inst)) for i in jmps]
    nops = [execute(change_op("jmp", i, inst)) for i in nops]

    jmps = next((res for (res, safe) in jmps if safe), None)
    nops = next((res for (res, safe) in nops if safe), None)

    n = jmps if jmps is not None else nops

    print(f"Part two: acc={n} with clean bruteforce")
