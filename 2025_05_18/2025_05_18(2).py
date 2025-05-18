import math as m

def primes(n: int) -> list:
  ret = [2,3]
  for index in range(2, n + 1):
    jud = True
    if index in ret:
      continue
    for ind in ret:
      if index % ind == 0:
        jud = False
    if jud:
      ret.append(index)
  return ret

def filter_primes(lst: list[int]) -> list[int]:
  l = sorted(lst, reverse=True)
  maxi = l[0]
  l = sorted(lst)
  ma = primes(maxi)
  ret = []
  for index in lst:
    if index in ma:
      ret.append(index)
  return ret

print(filter_primes([2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(filter_primes([11, 13, 17, 19, 21, 23]))