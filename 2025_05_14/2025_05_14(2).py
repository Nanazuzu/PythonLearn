def remove_duplicates(s: str) -> str:
  ret = []
  for index in s:
    if index not in ret:
      ret.append(index)
  return ''.join(ret)

# not in IS O(2^n)
#THIS CODE CAN CHANGE WITH USE SET

print(remove_duplicates("banana"))
print(remove_duplicates("aabbcc"))
print(remove_duplicates("abcabcabc"))