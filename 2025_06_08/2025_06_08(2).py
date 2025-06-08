def two_sum_combinations(nums: list[int]) -> list[int]:
  ret = set()
  for index in nums:
    for i in nums:
      if i == index:
        continue
      ret.add(i + index)
  return sorted(list(ret))

print(two_sum_combinations([2, 1, 3, 4, 1]))
print(two_sum_combinations([5, 0, 2, 7]))