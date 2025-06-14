def forgotten_words(original: list[str], remembered: list[str]) -> list[str]:
  origin = set(original)
  mem = set(remembered)
  return sorted(list(origin - mem))

print(forgotten_words(["apple", "banana", "carrot", "date", "eggplant"], ["banana", "eggplant", "apple"]))
print(forgotten_words(["hello", "world", "memory", "gone"], ["hello", "memory"]))