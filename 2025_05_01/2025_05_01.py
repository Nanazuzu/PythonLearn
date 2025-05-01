def most_frequent_number(nums: list[int]) -> int:
  seq_num = {}
  for index in nums:
    if index not in seq_num.keys():
      seq_num[index] = 1
    else:
      seq_num[index] += 1
  mid_seq_num = list(seq_num.keys())
  res = mid_seq_num[0]
  for indi in mid_seq_num:
    if seq_num[res] < seq_num[indi]:
      res = indi
    elif seq_num[res] == seq_num[indi]:
      if indi < res:
        res = indi
  return res

#CAN MAKE MORE EASIER
# from collections import Counter

# def most_frequent_number(nums):
#     counts = Counter(nums)
#     return min([k for k, v in counts.items() if v == max(counts.values())])

print(most_frequent_number([1,3,1,3,2,1]))
print(most_frequent_number([5,5,4,6,6]))
print(most_frequent_number([9]))