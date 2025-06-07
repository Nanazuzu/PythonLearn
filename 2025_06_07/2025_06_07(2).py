def max_profit(prices: list[int]) -> int:
  profit = 0
  index = {}
  for i, n in zip(prices, range(len(prices))):
    index[i] = n
  starts = sorted(list(index.keys()))
  start = index[starts[0]]
  for i in prices[start + 1:]:
    profit = max(profit, i - prices[start])
  return profit

#IT IS HARD CODING
# def max_profit(prices: list[int]) -> int:
#     min_price = float('inf')
#     max_profit = 0
    
#     for price in prices:
#         min_price = min(min_price, price)
#         max_profit = max(max_profit, price - min_price)
    
#     return max_profit
#it will be work.

print(max_profit([7,1,5,3,6,4]))
print(max_profit([7,6,4,3,1]))
print(max_profit([1,2,3,4,5]))