def smaller_after_reverse(n: int) -> int:
  e = 0
  list_num =[]
  while(True):
    if n // (10 ** e) != 0:
      e += 1
    else:
      e -= 1
      break
  indi = n
  for index in range(e, -1, -1):
    if indi // (10 ** index) == 0:
      continue
    num = indi // (10 ** index)
    list_num.append(num)
    indi %= 10 ** index
  revn = 0
  for ind in range(len(list_num)):
    revn += list_num[ind] * (10 ** ind)
  if n < revn:
    return n
  else:
    return revn
  
  # EASIER WAY: revn = int(str(n)[::-1])
  
print(smaller_after_reverse(123))
print(smaller_after_reverse(321))
print(smaller_after_reverse(700))
print(smaller_after_reverse(90))