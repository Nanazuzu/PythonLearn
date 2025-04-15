def sum_of_digits(n: int, digits: str) -> int:
  if n != len(digits):
    print("Input str is not equal length.\n")
    return -1
  digits_sum = 0
  for ch in digits:
    digits_sum += int(ch)
  return digits_sum

print(sum_of_digits(5, "54321"))
print(sum_of_digits(3, "123"))
print(sum_of_digits(4, "123"))
print(sum_of_digits(9, "123456789"))