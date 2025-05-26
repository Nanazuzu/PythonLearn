def largest_number(nums: list[int]) -> str:
  if list(set(nums)) == [0]:
    return "0"
  snum = []
  for index in nums:
    snum.append(str(index))
  ret = ""
  while 0 < len(snum):
    index = 0
    for ind in range(len(snum)):
      if len(snum[index]) == 1 and len(snum[ind]) == 1:
        if snum[index] < snum[ind]:
          index = ind
      elif 1 < len(snum[index]) and len(snum[ind]) == 1:
        if snum[index][0] < snum[ind]:
          index = ind
        elif snum[index][0] == snum[ind]:
          if snum[index][1] < snum[ind]:
            index = ind
      elif len(snum[index]) == 1 and 1 < len(snum[ind]):
        if snum[index] < snum[ind][0]:
          index = ind
        elif snum[index] == snum[ind][0]:
          if snum[index] < snum[ind][1]:
            index = ind
      else:
        if snum[index][0] < snum[ind][0]:
          index = ind
        elif snum[index][0] == snum[ind][0]:
          if snum[index][1] < snum[ind][1]:
            index = ind
    ret += snum.pop(index)
  return ret

#THIS IS HARDCODED ABOUT 2 DIGIT LIMITED.
# from functools import cmp_to_key

# def compare(a, b):
#     if a + b > b + a:
#         return -1
#     else:
#         return 1

# def largest_number(nums):
#     nums = list(map(str, nums))
#     nums.sort(key=cmp_to_key(compare))
#     result = ''.join(nums)
#     return '0' if result[0] == '0' else result
#this will work all digit.

print(largest_number([10, 2]))
print(largest_number([3, 30, 34, 5, 9]))
print(largest_number([0, 0]))