def can_form_staircase(nums: list[int]) -> bool:
  num = sorted(nums)
  ret = True
  for index in range(0,len(num) - 1):
    if 1 < abs(num[index] - num[index + 1]):
      ret = False
      break
  return ret

print(can_form_staircase([1, 2, 3, 4, 5]))
print(can_form_staircase([1, 3, 2, 4]))
print(can_form_staircase([1, 2, 4, 6]))
print(can_form_staircase([5, 4, 4, 3]))