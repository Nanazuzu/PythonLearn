def longest_increasing_digits(s: str) -> str:
  msg = s
  start = 0
  end = 1
  dist = 0
  index = 0
  while(True):
    while(True):
      if end + 1 == len(msg):
        break
      if int(msg[end]) - int(msg[end - 1]) != 1:
        break
      end += 1
      if dist < end - start:
        dist = end - start
        index = start
    start = end
    if end + 1 == len(msg):
      break
    end += 1
  if dist == 0:
    return msg[0]
  res = []
  for ini in range(index, index + dist):
    res.append(msg[ini])
  return ''.join(res)

print(longest_increasing_digits("781234569"))
print(longest_increasing_digits("987654321"))
print(longest_increasing_digits("1231234567890"))