def split_even_odd(lst: list[int]) -> tuple[list[int], list[int]]:
  odd = []
  even = []
  for index in lst:
    if index % 2 == 0:
      even.append(index)
    else:
      odd.append(index)
  even = sorted(even)
  odd = sorted(odd)
  return (even, odd)

print(split_even_odd([5, 3, 2, 8, 1, 4]))
print(split_even_odd([7, 9, 11]))