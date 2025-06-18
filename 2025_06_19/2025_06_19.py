def custom_sort(arr: list[int], n: int) -> list[int]:
  return sorted(arr, key=lambda x : (abs(x - n), -x))

print(custom_sort([1, 2, 3, 4, 5], 3))
print(custom_sort([100, 50, 70, 70, 30], 60))