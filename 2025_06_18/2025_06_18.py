def most_common_letter(s: str) -> str:
  ret = {}
  l = s.lower()
  for index in l:
    if index not in ret.keys():
      ret[index] = 1
    else:
      ret[index] += 1
  res = sorted(ret.items(), key=lambda x : x[1], reverse=True)
  if res[0][1] == res[1][1]:
    return "?"
  return res[0][0]

print(most_common_letter("Mississipi"))
print(most_common_letter("zZa"))