def single_number(nums: list[int]) -> int:
  ret = 0
  for index in nums:
    ret = ret ^ index
  return ret

print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))
print(single_number([3, 4, 5, 6, 4, 5, 3]))