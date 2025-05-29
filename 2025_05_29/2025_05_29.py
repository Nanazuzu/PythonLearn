def count_visible_students(heights: list[int]) -> int:
  if len(heights) == 0:
    return 0
  ret = [heights[0]]
  for index in heights[1:]:
    if ret[-1] < index:
      ret.append(index)
  return len(ret)

print(count_visible_students([130, 135, 148, 140, 145, 150, 150, 153]))
print(count_visible_students([150, 145, 140, 135]))
print(count_visible_students([]))