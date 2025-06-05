def combination_sum_count(nums: list[int], target: int) -> int:
  dp = [0] * (target + 1)
  dp[0] = 1

  for index in range(1, target + 1):
    for num in nums:
      if 0 <= index - num:
        dp[index] += dp[index - num]
  return dp[target]

print(combination_sum_count([1, 2, 3], 4))