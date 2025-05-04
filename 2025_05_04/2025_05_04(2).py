def decompress(s: str) -> str:
  jud = [str(x) for x in range(10)]
  lst = []
  mid_str = []
  for index in s:
    if index in jud:
      if len(mid_str) == 0:
        lst.append(index)
      else:
        lst.append(''.join(mid_str))
        mid_str.clear()
        lst.append(index)
    elif (index == '(') or (index == ')'):
      if index == ')' and len(mid_str) != 0:
        lst.append(''.join(mid_str))
        mid_str.clear()
      continue
    else:
      mid_str.append(index)
  mid_str = lst
  string = ""
  while(len(mid_str)):
    spstr = mid_str.pop()
    spnum = int(mid_str.pop())
    string = spstr + string
    string *= spnum
  return string

print(decompress("3(ab)"))
print(decompress("2(a2(b))"))
print(decompress("3(x2(yz))"))