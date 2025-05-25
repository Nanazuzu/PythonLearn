def two_sum(nums: list[int], target: int) -> list[int]:
  fm = {}
  ret = []
  for index in range(len(nums)):
    fm[index] = nums[index]
  fl = list(fm.values())
  for index in range(len(fl) - 1):
    if target - fl[index] in fl[index + 1:]:
      ret.append(index)
      ret.append(fl.index(target-fl[index], index+1))
  return ret
#IT IS O(N^2)
# def two_sum(nums: list[int], target: int) -> list[int]:
#     seen = {}
#     for i, num in enumerate(nums):
#         complement = target - num
#         if complement in seen:
#             return [seen[complement], i]
#         seen[num] = i
#THIS CODE BE O(N)


print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
print(two_sum([3, 3], 6))