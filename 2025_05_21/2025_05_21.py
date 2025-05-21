def most_frequent_word(text: str) -> str:
  jud = [chr(x) for x in range(97,123)]
  tt = text.lower().split(' ')
  text_filtered = []
  for index in tt:
    mid = []
    for ind in index:
      if ind not in jud:
        continue
      mid.append(ind)
    text_filtered.append(''.join(mid))
  res = {}
  for index in text_filtered:
    if index not in res.keys():
      res[index] = 1
    else:
      res[index] += 1
  sor = sorted(res.items(), key=lambda x : x[1], reverse=True)
  return sor[0][0] or '""'

print(most_frequent_word("Hello, hello! How are you?"))
print(most_frequent_word("To be or not to be, that is the question."))
print(most_frequent_word(""))