def to_weird_case(s: str) -> str:
  cases = s.split(" ")
  res = ""
  for index in cases:
    cnt = 0
    for cha in index:
      if cnt % 2 == 0:
        res += cha.upper()
        cnt += 1
      else:
        res += cha.lower()
        cnt += 1
    res += " "
  return res

print(to_weird_case("python function check"))
print(to_weird_case("hello world to python"))