def minimum_operations(nums: list[int]) -> int:
  num = sorted(nums)
  cnt = 0
  while len(num) != 0:
    jud = []
    for index in range(len(num)):
      if num[index] == 0:
        jud.append(index)
    jud = sorted(jud, reverse=True)
    for index in jud:
      num.pop(index)
    if len(num) == 0:
      break
    m = num[0]
    for index in range(len(num)):
      num[index] -= m
    cnt += 1
  return cnt

print(minimum_operations([1, 5, 0, 3, 5]))
print(minimum_operations([0, 0, 0]))
print(minimum_operations([2, 2, 2]))