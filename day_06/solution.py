from functools import reduce
from operator import or_


def parse(group: str):
    return [set(person.strip()) for person in group.strip().split("\n")]


with open("input", "r") as f:
    groups = [parse(line) for line in f.read().split("\n\n")]

    unique_answers = [reduce(or_, group) for group in groups]
    count = reduce(lambda a, b: a + b, [len(group) for group in unique_answers])
    print(f"Part one: {count} unique answers")

    intersected_answers = [
        reduce(lambda a, b: a.intersection(b), group) for group in groups
    ]
    count = reduce(lambda a, b: a + b, [len(group) for group in intersected_answers])
    print(f"Part two: {count} intersected answers")
