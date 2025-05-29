def min_meeting_rooms(intervals: list[tuple[int, int]]) -> int:
  ret = 1
  inter = sorted(intervals, key=lambda x : x[1])
  for index in range(len(inter) - 1):
    ex = [x for x in range(inter[index][0], inter[index][1])]
    ne = [x for x in range(inter[index + 1][0], inter[index + 1][1])]
    for ind in ex:
      if ind in ne:
        ret += 1
        break
  return ret
#IT WILL BE FAST WITH
# def min_meeting_rooms(intervals):
#     starts = sorted(i[0] for i in intervals)
#     ends = sorted(i[1] for i in intervals)

#     s, e = 0, 0
#     used_rooms = 0
#     max_rooms = 0

#     while s < len(intervals):
#         if starts[s] < ends[e]:
#             used_rooms += 1
#             max_rooms = max(max_rooms, used_rooms)
#             s += 1
#         else:
#             used_rooms -= 1
#             e += 1

#     return max_rooms

print(min_meeting_rooms([(0, 30), (5, 10), (15, 20)]))
print(min_meeting_rooms([(7, 10), (2, 4)]))