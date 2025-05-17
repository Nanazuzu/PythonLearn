def reverse_number(n: int) -> int:
  number = str(n)[::-1]
  return int(number)

print(reverse_number(1234))
print(reverse_number(1200))
print(reverse_number(100))