def compress_string(s: str) -> str:
  string_sum = ""
  string_made = s + "\0"
  chara = s[0]
  cnt = 0
  for stri in string_made:
    if chara == stri:
      cnt += 1
    else:
      string_sum += chara
      string_sum += str(cnt)
      chara = stri
      cnt = 1
  if len(string_sum) > len(s):
    return s
  else:
    return string_sum

print(compress_string("aabbbcc"))
print(compress_string("a"))
print(compress_string("aaAAaa"))