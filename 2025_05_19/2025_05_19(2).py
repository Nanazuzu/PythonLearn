def elevator_simulation(requests: list[int]) -> list[str]:
  req = requests[::-1]
  start = '1'
  res = []
  while(len(req) != 0):
    end = str(req.pop())
    if start == end:
      continue
    res.append(start + ' -> ' + end)
    start = end
  return res

print(elevator_simulation([5, 2, 8]))