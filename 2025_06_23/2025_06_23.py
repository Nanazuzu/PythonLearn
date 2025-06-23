def find_anagram_indices(s: str, p: str) -> list[int]:
  left = 0
  right = len(p) - 1
  ret = []
  while right < len(s):
    if sorted(''.join(s[left:right + 1])) == sorted(''.join(p)):
      ret.append(left)
    right += 1
    left += 1
  return ret

print(find_anagram_indices("cbaebabacd", "abc"))
print(find_anagram_indices("abab", "ab"))