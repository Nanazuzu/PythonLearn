def robot_cleaner(start: int, left: int, right: int) -> int:
  ret = []
  index = start
  for i in range(start, left, -1):
    ret.append(i)
    index -= 1
  for i in range(index, right + 1):
    ret.append(i)
    index += 1
  return len(list(set(ret)))

print(robot_cleaner(5, 2, 8))
print(robot_cleaner(3, 1, 5))