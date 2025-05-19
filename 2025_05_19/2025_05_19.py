def group_anagrams(words: list[str]) -> list[list[str]]:
  w = words
  ret = []
  while(True):
    mid = []
    jud = []
    if len(w) == 0:
      break
    ind = w[0]
    for index in w:
      this_is_in = True
      for ini in ind:
        if ini not in index:
          this_is_in = False
      jud.append(this_is_in)
    for index in range(len(w)):
      if jud[index]:
        mid.append(w[index])
    for index in range(len(w) - 1, -1, -1):
      if jud[index]:
        w.pop(index)
    ret.append(mid)
  return ret

#It can make error
# from collections import defaultdict

# def group_anagrams(words: list[str]) -> list[list[str]]:
#     anagrams = defaultdict(list)
#     for word in words:
#         key = ''.join(sorted(word))
#         anagrams[key].append(word)
#     return list(anagrams.values())
#This code will be work well


print(group_anagrams(["bat", "tab", "eat", "tea", "tan", "nat", "ate"]))