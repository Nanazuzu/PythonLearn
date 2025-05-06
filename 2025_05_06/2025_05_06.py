def first_repeat_distances(s: str) -> dict[str, int]:
  s_m = {}
  s_b = {}
  res = {}
  for index in range(len(s)):
    if s[index] in s_m.keys() and not s_b[s[index]]:
      dist = index - s_m[s[index]]
      res[s[index]] = dist
      s_b[s[index]] = True
    else:
      s_m[s[index]] = index
      s_b[s[index]] = False
  return res

print(first_repeat_distances("abacbade"))
print(first_repeat_distances("nanazuzu"))