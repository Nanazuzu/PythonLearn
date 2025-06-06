def max_alternating_subarray(nums: list[int]) -> int:
  start = 0
  end = 1
  window = {}
  window[start] = nums[start]
  dist = 1
  while end < len(nums):
    if len(window.keys()) == 0:
      window[end] = nums[end]
      end += 1
      continue
    if nums[end] % 2 ^ window[end - 1] % 2 == 0:
      for index in range(start, end):
        window.pop(index)
        start += 1
      continue
    window[end] = nums[end]
    end += 1
    if dist < end - start:
      dist = end - start
  return dist

#SLIDING WINDOW HAS NOT TO USE
# prev_parity = nums[0] % 2
# curr_len = 1
# max_len = 1

# for i in range(1, len(nums)):
#     if nums[i] % 2 != prev_parity:
#         curr_len += 1
#     else:
#         curr_len = 1
#     prev_parity = nums[i] % 2
#     max_len = max(max_len, curr_len)
#this will be easier

print(max_alternating_subarray([1, 2, 3, 4, 5, 6]))
print(max_alternating_subarray([1, 3, 5, 7]))
print(max_alternating_subarray([2, 2, 2, 2]))
print(max_alternating_subarray([1, 2, 2, 3, 4, 5]))