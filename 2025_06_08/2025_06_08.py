def most_common_word(paragraph: str, banned: list[str]) -> str:
  jud = [chr(x) for x in range(97, 123)]
  char = paragraph.lower()
  lindex = []
  for index in range(len(char)):
    if char[index] not in jud and char[index] != ' ':
      lindex.append(index)
  for index in lindex[::-1]:
    char = char[:index] + char[index + 1:]
  splited_char = char.split(' ')
  lindex.clear()
  for index in range(len(splited_char)):
    if splited_char[index] in banned:
      lindex.append(index)
  for index in lindex[::-1]:
    splited_char.pop(index)
  ret = {}
  for index in splited_char:
    if index not in ret.keys():
      ret[index] = 1
    else:
      ret[index] += 1
  res = sorted(ret.items(), key=lambda x : x[1], reverse=True)
  return res[0][0]

#USE MODULE
# import re
# char = re.sub(r"[!?',;.\"]", " ", paragraph.lower())
# from collections import Counter
# counter = Counter(splited_char)
# res = counter.most_common(1)[0][0]


paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(most_common_word(paragraph, banned))