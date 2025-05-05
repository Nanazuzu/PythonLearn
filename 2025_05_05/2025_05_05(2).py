def clean_toy_names(names: list[str]) -> list[str]:
  juds = [chr(x) for x in range(97, 123)]
  toys = []
  for index in names:
    mid = []
    if not index.islower(): #String is immutable, so MUST USE RETURN VALUE
      seq = index.lower()
    else:
      seq = index
    for ini in seq:
      if ini in juds:
        mid.append(ini)
    if len(mid) != 0:
      toys.append(''.join(mid))
      mid.clear()
  toy = set()
  for ide in toys:
    toy.add(ide)
  return sorted(list(toy))

print(clean_toy_names(["6", "Teddy Bear", "lego", "LEG O", "  teddy  bear", "robot", "robot"]))