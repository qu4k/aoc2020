def find(numbers):
  for y in numbers:
    for x in numbers:
      if x + y == 2020:
        return [x, y]

with open("input.nlist", "r") as f:
  numbers = [int(i) for i in f.readlines()]
  n1, n2 = find(numbers)
  print(f"{n1} * {n2} = {n1 * n2}")