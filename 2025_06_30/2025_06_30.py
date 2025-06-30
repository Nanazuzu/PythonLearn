def max_stair_score(scores: list[int]) -> int:
  dp = []
  dp.append(scores[0])
  dp.append(scores[0] + scores[1])
  dp.append(max(scores[0] + scores[2], scores[1] + scores[2]))
  for index in range(3, len(scores)):
    dp.append(max(dp[index - 2] + scores[index], dp[index - 3] + scores[index - 1] + scores[index]))
  return dp[len(scores) - 1]

print(max_stair_score([10, 20, 15, 25, 10, 20]))