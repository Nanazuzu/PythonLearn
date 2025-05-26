def is_palindrome(s: str) -> bool:
  return s == s[::-1]

def longest_palindrome(s: str) -> str:
  if len(s) == 1 or (len(s) == 2 and s == s[::-1]):
    return s
  ret = ""
  for index in range(len(s)):
    for jud in range(index, len(s)):
      ss = s[index:jud + 1]
      if is_palindrome(ss) and len(ret) < len(ss):
        ret = ss
  return ret

print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("a"))
print(longest_palindrome("ac"))