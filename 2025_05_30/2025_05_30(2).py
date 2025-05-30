def find_max_average(nums: list[int], k: int) -> float:
  start = 0
  maxed = 0
  for _ in range(len(nums) - k + 1):
    end = start + k - 1
    sumed = sum(nums[start:end + 1])
    if maxed < sumed:
      maxed = sumed
    start += 1
  return round(maxed / k, 5)
#IT WILL BE FASTER WITH SLIDING WINDOW

print(find_max_average([1,12,-5,-6,50,3], 4))
print(find_max_average([5], 1))