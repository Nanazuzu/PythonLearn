def zero_erase_difference(n: int) -> int:
  e = 0
  list_num = []
  f = n
  while(True):
    if n // 10 ** e != 0:
      e += 1
    else:
      e -= 1
      break
  for index in range(e, -1, -1):
    if f // 10 ** index == 0:
      continue
    i = f
    i //= 10 ** index
    list_num.append(i)
    f %= 10 ** index
  sum_list = 0
  cnt = 0
  for ide in range(len(list_num) - 1, -1, -1):
    sum_list += list_num[cnt] * (10 ** ide)
    cnt += 1
  return n - sum_list

print(zero_erase_difference(10203))
print(zero_erase_difference(500600))
print(zero_erase_difference(123))