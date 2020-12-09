import re
from functools import reduce

re_rule = re.compile(r"([a-z ]+) bags contain (?:no other bags|([a-z1-9, ]+))\.")
re_bags = re.compile(r"(\d*) ([a-z ]+) bags?")


def parse(line: str) -> tuple:
    head = re_rule.match(line)
    name, bags = head.groups()
    if bags is None:
        return (name, bags)
    bags = [re_bags.match(bag).groups() for bag in bags.split(", ")]
    return (name, {k: int(v) for v, k in bags})


def contains(needle: str, haystack: dict, rules: dict) -> bool:
    if haystack is None:
        return False
    elif needle in haystack:
        return True
    return any(
        map(
            lambda x: contains(needle, rules[x], rules),
            [name for name, _ in haystack.items()],
        )
    )


def count_bags(bag: dict, rules: dict) -> int:
    if bag is None:
        return 0
    return reduce(
        lambda a, b: a + b,
        [n for _, n in bag.items()]
        + [n * count_bags(rules[name], rules) for name, n in bag.items()],
    )


with open("input", "r") as f:
    rules = dict([parse(line) for line in f.readlines()])

    golden_bags = [
        bag for bag, rule in rules.items() if contains("shiny gold", rule, rules)
    ]

    print(f"Part one: {len(golden_bags)} bags can contain a shiny gold bag")

    count = count_bags(rules["shiny gold"], rules)
    print(f"Part one: {count} bags are contained in a shiny gold bag")
