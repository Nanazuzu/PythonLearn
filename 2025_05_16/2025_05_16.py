import math as m

def cnt_div(n: int) -> int:
  mid = int(m.sqrt(n))
  res = []
  for index in range(1, mid + 1):
    if n % index == 0:
      res.append(index)
      res.append(n // index)
  return len(list(set(res)))

def number_with_most_divisors(n: int) -> tuple[int, int]:
  mid = {}
  for index in range(1, n + 1):
    mid[index] = cnt_div(index)
  ret_n = sorted(mid.items(), key=lambda x : x[1], reverse=True)
  return ret_n[0]

print(number_with_most_divisors(10))