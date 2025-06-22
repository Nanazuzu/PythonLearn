from collections import defaultdict as diction

def group_anagrams(words: list[str]) -> list[list[str]]:
  mid = diction(list)
  for index in range(len(words)):
    mid[''.join(sorted((words[index])))].append(index)
  ret = []
  for index in mid.keys():
    suit = []
    for i in mid[index]:
      suit.append(words[i])
    ret.append(suit)
  return ret

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))