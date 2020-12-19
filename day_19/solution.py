import re
import collections

Or = collections.namedtuple("Or", "lhs rhs")


def parse_expr(expr: str) -> any:
    if '"' in expr:  # text expression
        return expr.replace('"', "")
    elif "|" in expr:  # or expression
        lhs, rhs = [p.strip() for p in expr.split("|")]
        return Or(parse_expr(lhs), parse_expr(rhs))
    else:  # reference expression
        return [int(e) for e in expr.split(" ")]


def parse_rule(rule: str) -> tuple:
    i, expr = [p.strip() for p in rule.split(":")]
    return (int(i), parse_expr(expr))


def coerce(expr: any, rules: dict, depth=0) -> str:
    if depth >= 100:
        return ""
    elif type(expr) is str:
        return expr
    elif type(expr) is int:
        return coerce(rules[expr], rules, depth + 1)
    elif isinstance(expr, Or):
        return f"({coerce(expr.lhs, rules, depth + 1)}|{coerce(expr.rhs, rules, depth + 1)})"
    else:
        return "".join([coerce(e, rules, depth + 1) for e in expr])


with open("input", "r") as f:
    rules, tests = [section.strip().split("\n") for section in f.read().split("\n\n")]
    rules = dict([parse_rule(rule) for rule in rules])

    regex = re.compile(f"^{coerce(rules[0], rules)}$")
    valid = len([True for test in tests if regex.match(test) is not None])
    print(f"Part one: {valid} are valid")

    rules[8] = Or([42], [42, 8])
    rules[11] = Or([42, 31], [42, 11, 31])

    regex = re.compile(f"^{coerce(rules[0], rules)}$")
    valid = len([True for test in tests if regex.match(test) is not None])
    print(f"Part two: {valid} are valid after rule mutation")
