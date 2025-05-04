def filter_words(words: list[str]) -> list[str]:
  jud_li = []
  motchr = ['a', 'e', 'i', 'o', 'u']
  for index in words:
    if len(index) < 5:
      continue
    if not index.islower():
      continue
    cnt = 0
    for char in index:
      if char in motchr:
        cnt += 1
    if cnt < 2:
      continue
    jud_li.append(index)
  if len(jud_li) == 0:
    return []
  else:
    return sorted(jud_li)
  
print(filter_words(["apple", "orange", "sky", "hello", "zoo", "linux"]))
print(filter_words(["why", "my", "try"]))