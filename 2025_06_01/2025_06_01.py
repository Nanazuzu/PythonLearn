def longest_unique_subarray(nums: list[int]) -> int:
  start = 0
  end = 1
  window = {}
  window[nums[start]] = start
  dist = 0
  while True:
    if len(nums) <= end:
      break
    if nums[end] in window.keys():
      for _ in range(start, window[nums[end]] + 1):
        window.pop(nums[_])
        start += 1
      continue
    window[nums[end]] = end
    end += 1
    if dist < end - start:
      dist = end - start
  return dist

print(longest_unique_subarray([4, 2, 1, 2, 3, 4, 5]))
print(longest_unique_subarray([1, 2, 3, 4, 5]))
print(longest_unique_subarray([1, 1, 1, 1]))