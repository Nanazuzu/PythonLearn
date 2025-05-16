import math as m

def prime(n: int) -> list[int]:
  res = [2, 3]
  for index in range(4, n + 1):
    is_prime = True
    for ind in res:
      if index % ind == 0:
        is_prime = False
    if is_prime:
      res.append(index)
  return res

def division(n: int) -> dict:
  pri = prime(n)
  div = []
  for index in range(len(pri)):
    if n % pri[index] == 0:
      div.append(pri[index])
  ret = {}
  num = n
  while(True):
    if len(div) == 0:
      break
    if num % div[0] != 0:
      div.pop(0)
    elif num % div[0] == 0:
      num = num // div[0]
      if div[0] not in list(ret.keys()):
        ret[div[0]] = 1
      else:
        ret[div[0]] += 1
  return ret

def common_divisors(a: int, b: int) -> list[int]:
  a_division = division(a)
  b_division = division(b)
  jh_a = set(list(a_division.keys()))
  jh_b = set(list(b_division.keys()))
  dup = list(jh_a & jh_b)
  if len(dup) == 0:
    return dup
  md = {}
  for index in dup:
    if a_division[index] <= b_division[index]:
      md[index] = a_division[index]
    else:
      md[index] = b_division[index]
  mdn = 1
  for index in list(md.keys()):
    mdn *= index ** md[index]
  ret = []
  for index in range(1, mdn + 1):
    if mdn % index == 0:
      ret.append(index)
  return ret

print(common_divisors(12, 18) or None)
print(common_divisors(7, 5) or None)