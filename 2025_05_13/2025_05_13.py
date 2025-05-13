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

def what_is_div(n: int) -> dict:
  cnt = int(m.sqrt(n))
  prime = primes(cnt)
  mid = []
  res = {}
  for index in prime:
    if n % index == 0:
      mid.append(index)
  if len(mid) == 0:
    res[1] = 1
    res[n] = 1
    return res
  for index in mid:
    res[index] = 0
  div = n
  while(True):
    if div % mid[0] == 0:
      res[mid[0]] += 1
      div /= mid[0]
    else:
      mid.pop(0)
    if len(mid) == 0:
      break
  return res

def gcd_lcm(a: int, b: int) -> tuple[int, int]:
  a_div = what_is_div(a)
  b_div = what_is_div(b)
  gcd = 1
  for index in list(a_div.keys()):
     if index not in list(b_div.keys()):
       continue
     if a_div[index] < b_div[index]:
       gcd *= index ** a_div[index]
     elif b_div[index] < a_div[index]:
       gcd *= index ** b_div[index]
     else:
       gcd *= index ** a_div[index]
  lcm = 1
  combine = list(set(list(a_div.keys()) + list(b_div.keys())))
  for index in combine:
    if index not in list(a_div.keys()):
      lcm *= index ** b_div[index]
    elif index not in list(b_div.keys()):
      lcm *= index ** a_div[index]
    else:
      if a_div[index] < b_div[index]:
        lcm *= index ** b_div[index]
      else:
        lcm *= index ** a_div[index]
  return (gcd, lcm)

#Easier way
# def gcd(a: int, b: int) -> int:
#     while b:
#         a, b = b, a % b
#     return a

# def lcm(a: int, b: int) -> int:
#     return a * b // gcd(a, b)

# print(gcd(12, 18))  # 6
# print(lcm(12, 18))  # 36


print(gcd_lcm(12, 18))
print(gcd_lcm(7, 5))