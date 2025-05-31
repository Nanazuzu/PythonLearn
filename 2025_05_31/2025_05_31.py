def frequency_sort(s: str) -> str:
  ret = {}
  for index in s:
    if index in ret.keys():
      ret[index] += 1
    else:
      ret[index] = 1
  sor = sorted(ret.items(), key=lambda x:x[1], reverse=True)
  res = []
  #PYTHON CAN DO ANYTHING
  for index in sor:
    for _ in range(index[1]):
      res.append(index[0])
  #THIS WILL BE
  # for char, cnt in sor:
  #   res.append(char * cnt)
  return ''.join(res)

print(frequency_sort("tree"))
print(frequency_sort("cccaaa"))
print(frequency_sort("Aabb"))