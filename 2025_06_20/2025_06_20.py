def three_sum_zero(nums: list[int]) -> int:
  num = sorted(nums)
  ret = []
  for left in range(len(nums) - 1):
    for right in range(1, len(nums)):
      if left == right:
        continue
      if -1 * (nums[left] + nums[right]) in nums:
        i = nums.index(-1 * (nums[left] + nums[right]))
        if i == left or i == right:
          continue
        ret.append(sorted([nums[left], nums[right], -1 * (nums[left] + nums[right])]))
  tmp = []
  for index in ret:
    if index not in tmp:
      tmp.append(index)
  return len(tmp)
#IT WILL BE SLOW
# def three_sum_zero(nums: list[int]) -> int:
#     nums.sort()
#     result = set()
#     for i in range(len(nums)):
#         left = i + 1
#         right = len(nums) - 1
#         while left < right:
#             s = nums[i] + nums[left] + nums[right]
#             if s == 0:
#                 result.add((nums[i], nums[left], nums[right]))
#                 left += 1
#                 right -= 1
#             elif s < 0:
#                 left += 1
#             else:
#                 right -= 1
#     return len(result)
#this will be work faster

print(three_sum_zero([-1, 0, 1, 2, -1, -4]))