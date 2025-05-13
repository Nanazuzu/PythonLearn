def compress_list(lst: list[int]) -> list[int]:
  ret = []
  for index in lst:
    if index not in ret:
      ret.append(index)
    else:
      if index != ret[-1]:
        ret.append(index)
  return ret

#It can be O(n^2)
#Use like this
# def compress_list(lst: list[int]) -> list[int]:
#     ret = []
#     prev = None
#     for index in lst:
#         if index != prev:
#             ret.append(index)
#             prev = index
#     return ret


print(compress_list([1, 1, 2, 2, 2, 3, 1, 1, 4]))
print(compress_list([5, 5, 5, 5, 5]))
print(compress_list([1, 2, 3, 4]))