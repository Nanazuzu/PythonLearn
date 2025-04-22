def sum_numbers_in_string(s: str) -> int:
  digit = ["0","1","2","3","4","5","6","7","8","9"]
  mid = []
  res = []
  cnt = 0
  s += "end"
  for i in s:
    if i in digit:
      mid.append(int(i))
      cnt += 1
    else:
      if(cnt == 0):
        continue
      sym = 0
      list_for_calc = mid[::-1]
      while(cnt != 0):
        sym += list_for_calc.pop() * (10 ** (cnt - 1))
        cnt -= 1
      res.append(sym)
      mid.clear()
  sum_of_num = 0
  for i in res:
    sum_of_num += i
  return sum_of_num
  
print(sum_numbers_in_string("aAb123c9z"))
print(sum_numbers_in_string("abc1d2e3"))
print(sum_numbers_in_string("abc"))