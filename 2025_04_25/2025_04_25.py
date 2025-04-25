def count_fashion_combinations(clothes: list[list[str]]) -> int:
  cate = 0
  cate_str = []
  cate_map = {}
  for l in range(len(clothes)):
    if not(clothes[l][1] in cate_str):
      cate += 1
      cate_str.append(clothes[l][1])
      cate_map[clothes[l][1]] = list()
      cate_map[clothes[l][1]].append(clothes[l][0])
    else:
      cate_map[clothes[l][1]].append(clothes[l][0])
  res = 1
  for index in cate_str:
    intd = len(cate_map[index]) + 1
    res *= intd
  res -= 1
  return res

print(count_fashion_combinations([["yellow_hat", "headgear"],["blue_sunglasses", "eyewear"],["green_turban", "headgear"]]))
print(count_fashion_combinations([["mask", "face"],["sunglasses", "face"],["hat", "head"], ["pin","head"]]))