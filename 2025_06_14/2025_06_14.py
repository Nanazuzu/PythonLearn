def count_numbers(numbers: list[int]) -> dict:
  ret = {}
  for index in numbers:
    if index not in ret.keys():
      ret[index] = 1
    else:
      ret[index] += 1
  return sorted(ret.items(), key=lambda x : x[0])

print(count_numbers([1, 3, 2, 3, 4, 1, 2, 5, 3, 2]))
print(count_numbers([-1, 0, -1, 1, 0]))