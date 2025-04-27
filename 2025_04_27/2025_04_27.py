def sum_of_divisors(n: int) -> int:
  divisor = []
  for index in range(1, n // 2 + 1):
    if(n % index == 0):
      if index not in divisor:
        divisor.append(index)
        if n / index != index:
          divisor.append(n // index)
  sumd = 0
  for index in divisor:
    sumd += index
  return sumd

#It won't be use list.

# def sum_of_divisors(n: int) -> int:
#     sumd = 0
#     for index in range(1, int(n**0.5) + 1):
#         if n % index == 0:
#             sumd += index
#             if index != n // index:
#                 sumd += n // index
#     return sumd


print(sum_of_divisors(12))
print(sum_of_divisors(5))