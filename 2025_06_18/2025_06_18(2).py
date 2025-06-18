def is_subsequence(a: str, b: str) -> str:
  ret = False
  cnt = 0
  for index in b:
    if a[cnt] == index:
      cnt += 1
      if len(a) == cnt:
        ret = True
        break
  if ret:
    return "yes"
  else:
    return "no"
  
print(is_subsequence("ace", "abcde"))
print(is_subsequence("aec", "abcde"))