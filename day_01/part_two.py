def find(numbers):
  for z in numbers:
    for y in numbers:
      for x in numbers:
        if x + y + z == 2020:
          return [x, y, z]

with open("input.nlist", "r") as f:
  numbers = [int(i) for i in f.readlines()]
  n1, n2, n3 = find(numbers)
  print(f"{n1} * {n2} * {n3} = {n1 * n2 * n3}")