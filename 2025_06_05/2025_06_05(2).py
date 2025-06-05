def custom_sort(words: list[str], n: int) -> list[str]:
  return sorted(words, key=lambda x: (x[n], x))

print(custom_sort(["sun", "bed", "car"], 1))
print(custom_sort(["abce", "abcd", "cdx"], 2))