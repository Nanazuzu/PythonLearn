import math as m

def what_is_prime(n: int) -> list[int]:
  ret = [2, 3]
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

def is_prime(n: int) -> bool:
  number = n
  if number % 2 == 0 and number != 2:
    return False
  jud = int(m.sqrt(number))
  prime = what_is_prime(jud)
  ret = True
  for index in prime:
    if n % index == 0:
      ret = False
      break
  return ret

print(is_prime(199))
print(is_prime(14))
print(is_prime(103))
print(is_prime(120))
print(is_prime(307))
print(is_prime(809))
print(is_prime(324))
print(is_prime(945))