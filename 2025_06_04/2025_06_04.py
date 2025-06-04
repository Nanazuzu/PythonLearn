def count_frequencies(nums: list[int]) -> list[int]:
  ret = []
  for _ in range(101):
    ret.append(0)
  for index in nums:
    ret[index] += 1
  return ret

print(count_frequencies([1, 2, 2, 3, 99, 100]))
print(count_frequencies([0, 0, 0]))