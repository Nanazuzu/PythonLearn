def climb_stairs(n: int) -> int:
  d = [0] * 100
  d[1] = 1
  d[2] = 2
  l = 45
  for i in range(3, l + 1):
    d[i] = d[i - 1] + d[i - 2]
  return d[n]

print(climb_stairs(5))
print(climb_stairs(3))
print(climb_stairs(8))