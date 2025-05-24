def coin_change(coins: list[int], amount: int) -> int:
  con = sorted(coins, reverse=True)
  cnt = 0
  amt = amount
  while(amt >= 0):
    if len(con) == 0:
      break
    if amt - con[0] < 0:
      con.pop(0)
    else:
      amt -= con[0]
      cnt += 1
  if amt != 0:
    return -1
  return cnt

#THIS IS ANSWER
# def coin_change(coins: list[int], amount: int) -> int:
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0
#     for coin in coins:
#         for x in range(coin, amount + 1):
#             dp[x] = min(dp[x], dp[x - coin] + 1)
#     return dp[amount] if dp[amount] != float('inf') else -1

print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))