def remove_duplicate_chars(s: str) -> str:
  res = []
  res.append(s[0])
  for index in s:
    if index in res:
      continue
    res.append(index)
  ret = ""
  for index in res:
    ret += index
  return ret

print(remove_duplicate_chars("banana"))
print(remove_duplicate_chars("abcabcabc"))
print(remove_duplicate_chars("aabbccddeeff"))