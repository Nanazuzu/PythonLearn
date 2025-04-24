def find_nearest_same_char(s: str) -> list[int]:
  char = {}
  res = []
  cnt = 0
  for word in s:
    if(word in char):
      index = char.get(word)
      res.append(cnt - index)
      char[word] = cnt
      cnt += 1
    else:
      res.append(-1)
      char[word] = cnt
      cnt += 1
  return res

print(find_nearest_same_char("banana"))
print(find_nearest_same_char("tomato"))
print(find_nearest_same_char("potato"))