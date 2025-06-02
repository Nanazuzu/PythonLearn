def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
  inter = sorted(intervals, key=lambda x: x[0])
  ret = []
  start = inter[0][0]
  end = inter[0][1]
  for index in inter[1:]:
    if index[0] <= end:
      end = index[1]
    else:
      ret.append((start, end))
      start = index[0]
      end = index[1]
  ret.append((start,end))
  return ret

print(merge_intervals([(1, 3), (2, 6), (8, 10), (15, 18)]))
print(merge_intervals([(1, 4), (4, 5)]))