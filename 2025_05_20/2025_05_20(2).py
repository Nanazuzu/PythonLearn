def find_largest_number_with_same_digit_sum(n: int) -> int:
  e = 0
  while 10 ** e <= n:
    e += 1
  num = str(n)
  sumd = 0
  for index in num:
    sumd += int(index)
  digit_sum_target = sumd
  answer = 0
  for index in range(n, -1, -1):
    if sum(map(int, str(index))) == digit_sum_target:
        answer = index
        break
  return answer

print(find_largest_number_with_same_digit_sum(123))
print(find_largest_number_with_same_digit_sum(99))
print(find_largest_number_with_same_digit_sum(321))
print(find_largest_number_with_same_digit_sum(1000))
print(find_largest_number_with_same_digit_sum(86))
print(find_largest_number_with_same_digit_sum(111))