def word_length_statistics(s: str) -> dict[int, int]:
  jud = [chr(x) for x in range(97, 123)]
  sl = s.split(' ')
  middle = []
  for index in sl:
    index = index.lower()
    mid = []
    for ind in index:
      if ind in jud:
        mid.append(ind)
    middle.append(len(mid))
  cnt = {}
  for index in middle:
    if index not in cnt.keys():
      cnt[index] = 1
    else:
      cnt[index] += 1
  return sorted(cnt.items())

print(word_length_statistics("This is a simple sentence, with some punctuation."))