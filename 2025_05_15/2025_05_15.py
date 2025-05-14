def range_sums(lst: list[int], queries: list[tuple[int, int]]) -> list[int]:
  res = []
  for _ in range(len(queries)):
    mid = []
    start = queries[_][0]
    end = queries[_][1]
    mid = (lst[start:end+1])
    ret = 0
    for index in mid:
      ret += index
    res.append(ret)
  return res

# EASIER WAY
# return [sum(lst[start:end+1]) for start, end in queries]

print(range_sums([1,2,3,4,5], [(0,2),(1,3),(2,4)]))