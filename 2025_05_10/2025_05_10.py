def read_number_in_korean(n: int) -> str:
  jud = {}
  korean = ["공", "일", "이", "삼", "사", "오", "육", "칠", "팔", "구"]
  for index in range(10):
    jud[index] = korean[index]
  e = 0
  num = n
  while(True):
    if num // (10 ** e) == 0:
      e -= 1
      break
    e += 1
  res = []
  for index in range(e, -1, -1):
    number = num // (10 ** index)
    res.append(jud[number])
    num -= number * (10 ** index)
    res.append(' ')
  return ''.join(res)  #return ' '.join(res) will easier way.

print(read_number_in_korean(1024))
print(read_number_in_korean(7))
print(read_number_in_korean(6667248))