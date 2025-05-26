def max_meetings(intervals: list[tuple[int, int]]) -> int:
  inter = sorted(intervals, key=lambda x : x[1])
  ret = [inter[0]]
  for ind in inter:
    ex = [x for x in range(ret[-1][0], ret[-1][1])]
    ne = [x for x in range(ind[0], ind[1])]
    jud = True
    for ini in ex:
      if ini in ne:
        jud = False
        break
    if jud:
      ret.append(ind)
  return ret

print(max_meetings([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(max_meetings([(1, 3), (2, 4), (3, 5)]))
print(max_meetings([(7, 9), (0, 10), (4, 5), (8, 9), (4, 10), (5, 7)]))