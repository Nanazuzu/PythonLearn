def word_frequency(s: str) -> None:
  res = {}
  jud = [chr(x) for x in range(97,123)]
  mid = []
  string = s
  string = string.lower()
  strings = string.split(' ')
  for index in strings:
    rem = []
    for ind in index:
      if ind in jud:
        rem.append(ind)
    mid.append(''.join(rem))
  for index in mid:
    if index not in list(res.keys()):
      res[index] = 1
    else:
      res[index] += 1
  res_sort_key = dict(sorted(res.items()))
  res_sort = dict(sorted(res_sort_key.items(), key=lambda x:x[1], reverse=True))
  print(res_sort)
  #It will be better to see outputs.
  # for word, count in res_sort.items():
  #   print(f"{word} - {count}")

word_frequency("Hello world! Hello, world. hello?")
word_frequency("This is a test. This is only a test.")