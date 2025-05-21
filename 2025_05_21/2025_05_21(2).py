from itertools import combinations as cb

def best_score_combination(scores: list[int], limit: int) -> int:
  ob = cb(scores, 3)
  ret = 0
  for index in ob:
    if limit < sum(index):
      continue
    if ret < sum(index):
      ret = sum(index)
  return ret

print(best_score_combination([60, 50, 70, 90, 30], 200))
print(best_score_combination([40, 40, 40], 100))
print(best_score_combination([5, 1, 3, 7, 9], 15))