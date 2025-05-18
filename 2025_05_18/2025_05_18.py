def filter_and_sort(lst: list[int], low: int, high: int) -> list[int]:
  ret = []
  for index in lst:
    if low <= index <= high:
      ret.append(index)
  return sorted(ret)

print(filter_and_sort([5, 1, 9, 3, 7, 2], 3, 7))
print(filter_and_sort([10, 20, 30, 40], 15, 35))