def count_uppercase_words(s: str) -> int:
  string = s.split(' ')
  ret = 0
  for index in string:
    if index.isupper():
      ret += 1
  return ret

print(count_uppercase_words("THIS is a TEST STRING for YOU"))
print(count_uppercase_words("HeLLo WOrLD"))
print(count_uppercase_words("WELCOME TO THE JUNGLE"))