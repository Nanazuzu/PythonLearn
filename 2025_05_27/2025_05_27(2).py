def max_subarray_sum(nums: list[int]) -> int:
  # ret = 0
  # maxed = 0
  # for index in nums:
  #   if index <= index + maxed:
  #     maxed += index
  #   if ret < maxed:
  #     ret = maxed
  #IT FAILS IN START NEGATIVE
  ret = maxed = nums[0]
  for index in nums[1:]:
    maxed = max(index, index + maxed)
    ret = max(maxed, ret)
  return ret

print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))
print(max_subarray_sum([1]))
print(max_subarray_sum([5,4,-1,7,8]))