def lru_words(capacity: int, words: list[str]) -> list[str]:
  ret = []
  for index in words:
    if index in ret:
      i = ret.index(index)
      ret.pop(i)
      ret.insert(0, index)
    else:
      ret.insert(0, index)
    if capacity < len(ret):
      ret.pop()
  return ret

print(lru_words(5, ["apple", "banana", "apple", "carrot", "banana", "egg", "date"]))
print(lru_words(3, ["a", "b", "a", "c", "d"]))