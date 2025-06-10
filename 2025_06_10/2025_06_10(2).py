def word_sort(words: list[str]) -> list[str]:
  ret = {}
  for index in words:
    ret[index] = len(index)
  return [word for word, _ in sorted(ret.items(), key=lambda x: (x[1], x[0]))]

print(word_sort(["but", "i", "wont", "hesitate", "no", "more", "no", "more", "it", "cannot", "wait", "im", "yours"]))