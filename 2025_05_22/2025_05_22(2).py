def compress_numbers(nums: list[int]) -> list[tuple[int, int]]:
  mid = []
  num = 0
  cnt = 0
  for index in nums:
    if index != num and cnt == 0:
      num = index
      cnt = 1
    elif index == num:
      cnt += 1
    else:
      mid.append((num, cnt))
      num = index
      cnt = 1
  mid.append((num, cnt))
  return mid

print(compress_numbers([1, 1, 2, 2, 2, 3, 1, 1]))
print(compress_numbers([5, 5, 5, 5]))
print(compress_numbers([7, 8, 9]))