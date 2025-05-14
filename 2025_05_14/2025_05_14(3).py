def sort_words(s: str) -> str:
  org = s.split(' ')
  string = s.lower()
  inputd = sorted(string.split(' '))
  for index in org:
    for ind in range(len(inputd)):
      if index.lower() == inputd[ind]:
        inputd[ind] = index
  return ' '.join(inputd)

print(sort_words("Banana apple Cherry"))
print(sort_words("dog Cat elephant bee Ant"))