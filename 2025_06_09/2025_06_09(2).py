def dedup_and_sort(numbers: str) -> list[int]:
  num = numbers.split(' ')
  for index in range(len(num)):
    num[index] = int(num[index])
  num = list(set(num))
  return sorted(num)
#USE PYTHON
# def dedup_and_sort(numbers: str) -> list[int]:
#     return sorted(set(int(n) for n in numbers.split()))

print(dedup_and_sort("4 1 3 3 2 4 5 1 6"))
print(dedup_and_sort("10 5 10 10 5 4 3 3 -1"))